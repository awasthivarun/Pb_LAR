from pathlib import Path
import csv
import json

import numpy as np
from ase.io import read


ROOT = Path("/pscratch/sd/a/awasthi/Pb_LAR")
SURFACE_RESULTS = ROOT / "analysis/surface_results.csv"
OUTPUT = ROOT / "analysis/explicit_water_states.csv"

OH_COVALENT_MAX_A = 1.25
PROTON_WELL_PBH_MIN_A = 3.0
H2_MAX_A = 0.95


def unit(vector):
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)

    if norm < 1e-12:
        raise ValueError("Cannot normalize a near-zero vector.")

    return vector / norm


def angle_deg(v1, v2):
    cosine = np.clip(np.dot(unit(v1), unit(v2)), -1.0, 1.0)
    return float(np.degrees(np.arccos(cosine)))


def format_float(value, digits=3):
    if value in ("", None):
        return "NA"

    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def load_harvest():
    if not SURFACE_RESULTS.is_file():
        return {}

    rows = {}

    with SURFACE_RESULTS.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["job_id"]] = row

    return rows


def surface_plane_z(atoms, pb_indices):
    z = np.array([atoms.positions[i, 2] for i in pb_indices])
    return float(np.median(np.sort(z)[-9:]))


def analyze_job(job_dir, metadata, harvest):
    structure_path = job_dir / "CONTCAR"

    if not structure_path.is_file():
        return None

    atoms = read(structure_path, format="vasp")
    atoms.set_pbc((True, True, False))

    symbols = np.array(atoms.get_chemical_symbols())

    pb_indices = np.where(symbols == "Pb")[0]
    o_indices = np.where(symbols == "O")[0]
    h_indices = np.where(symbols == "H")[0]

    if len(o_indices) == 0:
        return None

    surface_z = surface_plane_z(atoms, pb_indices)

    nearest_o = {}

    for h_idx in h_indices:
        distances = [
            atoms.get_distance(int(h_idx), int(o_idx), mic=True)
            for o_idx in o_indices
        ]

        local = int(np.argmin(distances))

        nearest_o[int(h_idx)] = {
            "o_idx": int(o_indices[local]),
            "distance_A": float(distances[local]),
        }

    water_h = [
        int(h_idx)
        for h_idx in h_indices
        if nearest_o[int(h_idx)]["distance_A"] <= OH_COVALENT_MAX_A
    ]

    nonwater_h = [
        int(h_idx)
        for h_idx in h_indices
        if int(h_idx) not in water_h
    ]

    water_counts = []
    oh_distances = []
    hoh_angles = []

    for o_idx in o_indices:
        assigned = [
            h_idx
            for h_idx in water_h
            if nearest_o[h_idx]["o_idx"] == int(o_idx)
        ]

        water_counts.append(len(assigned))

        for h_idx in assigned:
            oh_distances.append(
                float(atoms.get_distance(int(o_idx), h_idx, mic=True))
            )

        if len(assigned) == 2:
            v1 = atoms.get_distance(
                int(o_idx),
                assigned[0],
                mic=True,
                vector=True,
            )

            v2 = atoms.get_distance(
                int(o_idx),
                assigned[1],
                mic=True,
                vector=True,
            )

            hoh_angles.append(angle_deg(v1, v2))

    pb_h_distances = []
    pb_h_zrel = []
    nearest_pb_indices = []

    for h_idx in nonwater_h:
        distances = [
            atoms.get_distance(h_idx, int(pb_idx), mic=True)
            for pb_idx in pb_indices
        ]

        local = int(np.argmin(distances))

        pb_h_distances.append(float(distances[local]))
        nearest_pb_indices.append(int(pb_indices[local]))
        pb_h_zrel.append(float(atoms.positions[h_idx, 2] - surface_z))

    hh_distances = []

    for i, h1 in enumerate(h_indices):
        for h2 in h_indices[i + 1:]:
            hh_distances.append(
                float(atoms.get_distance(int(h1), int(h2), mic=True))
            )

    nonwater_to_water_h = []

    for h1 in nonwater_h:
        for h2 in water_h:
            nonwater_to_water_h.append(
                float(atoms.get_distance(h1, h2, mic=True))
            )

    nonwater_to_o = []

    for h_idx in nonwater_h:
        for o_idx in o_indices:
            nonwater_to_o.append(
                float(atoms.get_distance(h_idx, int(o_idx), mic=True))
            )

    harvest_row = harvest.get(metadata["job_id"], {})

    proton_well_like = any(
        distance > PROTON_WELL_PBH_MIN_A
        for distance in pb_h_distances
    )

    water_intact = (
        len(o_indices) > 0
        and len(water_counts) == len(o_indices)
        and all(count == 2 for count in water_counts)
    )

    expected_nonwater_h = (
        len(h_indices) - 2 * len(o_indices)
        if water_intact
        else None
    )

    if water_intact and len(nonwater_h) == 2 and not proton_well_like:
        chemistry_state = "intact_2H2O_plus_bound_PbH2"
    elif proton_well_like:
        chemistry_state = "proton_well_like_nonwater_H"
    elif not water_intact:
        chemistry_state = "water_not_intact_or_rearranged"
    elif expected_nonwater_h is not None and len(nonwater_h) != expected_nonwater_h:
        chemistry_state = "unexpected_H_assignment"
    else:
        chemistry_state = "other"

    return {
        "job_id": metadata["job_id"],
        "status": harvest_row.get("status", ""),
        "final_fmax_eV_A": harvest_row.get("final_fmax_eV_A", ""),
        "target_mu_Ha": metadata.get("target_mu_Ha", ""),
        "water_orientation": metadata.get("water_orientation", ""),
        "chemistry_state": chemistry_state,
        "n_Pb": len(pb_indices),
        "n_O": len(o_indices),
        "n_H_total": len(h_indices),
        "n_water_H": len(water_h),
        "n_nonwater_H": len(nonwater_h),
        "water_H_counts_per_O": ";".join(str(x) for x in water_counts),
        "water_intact": water_intact,
        "OH_min_A": min(oh_distances) if oh_distances else "",
        "OH_max_A": max(oh_distances) if oh_distances else "",
        "HOH_angles_deg": ";".join(f"{x:.3f}" for x in hoh_angles),
        "PbH_min_A": min(pb_h_distances) if pb_h_distances else "",
        "PbH_max_A": max(pb_h_distances) if pb_h_distances else "",
        "nonwater_H_zrel_min_A": min(pb_h_zrel) if pb_h_zrel else "",
        "nonwater_H_zrel_max_A": max(pb_h_zrel) if pb_h_zrel else "",
        "nonwater_H_nearest_Pb": ";".join(str(x) for x in nearest_pb_indices),
        "nonwater_H_same_Pb": (
            len(set(nearest_pb_indices)) == 1
            if nearest_pb_indices
            else ""
        ),
        "min_HH_A": min(hh_distances) if hh_distances else "",
        "H2_like": min(hh_distances) < H2_MAX_A if hh_distances else False,
        "min_nonwaterH_waterH_A": min(nonwater_to_water_h) if nonwater_to_water_h else "",
        "min_nonwaterH_O_A": min(nonwater_to_o) if nonwater_to_o else "",
        "proton_well_like_nonwater_H": proton_well_like,
        "directory": str(job_dir),
    }


def main():
    harvest = load_harvest()
    rows = []

    for metadata_path in ROOT.rglob("metadata.json"):
        metadata = json.loads(metadata_path.read_text())

        if metadata.get("family") != "proton_well_rescue":
            continue

        row = analyze_job(
            metadata_path.parent,
            metadata,
            harvest,
        )

        if row is not None:
            rows.append(row)

    rows.sort(
        key=lambda row: (
            float(row["target_mu_Ha"])
            if row["target_mu_Ha"] not in ("", None)
            else 999.0,
            row["job_id"],
        )
    )

    if not rows:
        raise RuntimeError("No explicit-water proton_well_rescue jobs found.")

    fieldnames = list(rows[0].keys())

    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)

    print("Explicit-water Pb-H states")
    print("==========================")

    for row in rows:
        mu = format_float(row["target_mu_Ha"], digits=5)
        oh_min = format_float(row["OH_min_A"])
        oh_max = format_float(row["OH_max_A"])
        pbh_min = format_float(row["PbH_min_A"])
        pbh_max = format_float(row["PbH_max_A"])

        print(
            f"{row['job_id']:>4}  "
            f"mu={mu:>8}  "
            f"status={row['status']:<21}  "
            f"water={row['water_H_counts_per_O'] or 'NA':<5}  "
            f"OH={oh_min}-{oh_max} A  "
            f"PbH={pbh_min}-{pbh_max} A  "
            f"H2={row['H2_like']}  "
            f"proton_well={row['proton_well_like_nonwater_H']}  "
            f"{row['chemistry_state']}"
        )

    print()
    print(f"Wrote: {OUTPUT}")


if __name__ == "__main__":
    main()