from pathlib import Path
import csv
import json

import numpy as np
from ase.io import read


ROOT = Path("/pscratch/sd/a/awasthi/Pb_LAR")
SURFACE_RESULTS = ROOT / "analysis/surface_results.csv"
OUTPUT = ROOT / "analysis/explicit_water_states.csv"

OH_COVALENT_MAX_A = 1.25
BOUND_PBH_MAX_A = 2.60
PROTON_WELL_PBH_MIN_A = 3.00
H2_MAX_A = 0.95
DETACHED_PB_LIFT_MIN_A = 4.0
LIFTED_PB_MIN_A = 0.25


def unit(vector):
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    if norm < 1e-12:
        raise ValueError("Cannot normalize a near-zero vector.")
    return vector / norm


def angle_deg(v1, v2):
    return float(np.degrees(np.arccos(np.clip(np.dot(unit(v1), unit(v2)), -1.0, 1.0))))


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
    with SURFACE_RESULTS.open(newline="") as handle:
        return {row["job_id"]: row for row in csv.DictReader(handle)}


def surface_plane_z(atoms, pb_indices):
    if len(pb_indices) == 0:
        raise ValueError("Cannot define a Pb surface plane without Pb atoms.")
    n_reference = min(9, len(pb_indices))
    z = atoms.positions[pb_indices, 2]
    return float(np.median(np.sort(z)[-n_reference:]))


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
        distances = np.array([atoms.get_distance(int(h_idx), int(o_idx), mic=True) for o_idx in o_indices])
        local = int(np.argmin(distances))
        nearest_o[int(h_idx)] = {"o_idx": int(o_indices[local]), "distance_A": float(distances[local])}

    water_h = [int(h_idx) for h_idx in h_indices if nearest_o[int(h_idx)]["distance_A"] <= OH_COVALENT_MAX_A]
    nonwater_h = [int(h_idx) for h_idx in h_indices if int(h_idx) not in water_h]

    water_counts = []
    oh_distances = []
    hoh_angles = []
    for o_idx in o_indices:
        assigned = [h_idx for h_idx in water_h if nearest_o[h_idx]["o_idx"] == int(o_idx)]
        water_counts.append(len(assigned))
        oh_distances.extend(float(atoms.get_distance(int(o_idx), h_idx, mic=True)) for h_idx in assigned)
        if len(assigned) == 2:
            v1 = atoms.get_distance(int(o_idx), assigned[0], mic=True, vector=True)
            v2 = atoms.get_distance(int(o_idx), assigned[1], mic=True, vector=True)
            hoh_angles.append(angle_deg(v1, v2))

    pb_h_distances = []
    pb_h_zrel = []
    nearest_pb_indices = []
    nearest_pb_lifts = []
    for h_idx in nonwater_h:
        distances = np.array([atoms.get_distance(h_idx, int(pb_idx), mic=True) for pb_idx in pb_indices])
        local = int(np.argmin(distances))
        nearest_pb = int(pb_indices[local])
        pb_h_distances.append(float(distances[local]))
        nearest_pb_indices.append(nearest_pb)
        pb_h_zrel.append(float(atoms.positions[h_idx, 2] - surface_z))
        nearest_pb_lifts.append(float(atoms.positions[nearest_pb, 2] - surface_z))

    nonwater_hh = ""
    if len(nonwater_h) == 2:
        nonwater_hh = float(atoms.get_distance(nonwater_h[0], nonwater_h[1], mic=True))

    all_hh = [
        float(atoms.get_distance(int(h1), int(h2), mic=True))
        for i, h1 in enumerate(h_indices)
        for h2 in h_indices[i + 1:]
    ]
    nonwater_to_water_h = [float(atoms.get_distance(h1, h2, mic=True)) for h1 in nonwater_h for h2 in water_h]
    nonwater_to_o = [
        float(atoms.get_distance(h_idx, int(o_idx), mic=True)) for h_idx in nonwater_h for o_idx in o_indices
    ]

    water_intact = (
        len(water_counts) == len(o_indices) and len(o_indices) > 0 and all(count == 2 for count in water_counts)
    )
    same_pb = len(nearest_pb_indices) == 2 and nearest_pb_indices[0] == nearest_pb_indices[1]
    proton_well_like = any(distance > PROTON_WELL_PBH_MIN_A for distance in pb_h_distances)
    bound_to_pb = len(pb_h_distances) == 2 and max(pb_h_distances) <= BOUND_PBH_MAX_A
    h2_like = nonwater_hh != "" and nonwater_hh < H2_MAX_A
    common_pb_lift = nearest_pb_lifts[0] if same_pb else ""

    if not water_intact:
        chemistry_state = "water_not_intact_or_rearranged"
    elif len(nonwater_h) != 2:
        chemistry_state = "unexpected_H_assignment"
    elif h2_like:
        chemistry_state = "H2_like_nonwater_H"
    elif proton_well_like:
        chemistry_state = "proton_well_like_nonwater_H"
    elif bound_to_pb and same_pb and common_pb_lift >= DETACHED_PB_LIFT_MIN_A:
        chemistry_state = "intact_2H2O_plus_detached_PbH2"
    elif bound_to_pb and same_pb and common_pb_lift >= LIFTED_PB_MIN_A:
        chemistry_state = "intact_2H2O_plus_lifted_PbH2"
    elif bound_to_pb and same_pb:
        chemistry_state = "intact_2H2O_plus_surface_PbH2"
    elif bound_to_pb:
        chemistry_state = "intact_2H2O_plus_separated_surface_2H"
    else:
        chemistry_state = "intact_water_ambiguous_nonwater_H"

    harvest_row = harvest.get(metadata.get("job_id"), {})
    return {
        "job_id": metadata.get("job_id", ""),
        "family": metadata.get("family", ""),
        "status": harvest_row.get("status", ""),
        "final_fmax_eV_A": harvest_row.get("final_fmax_eV_A", ""),
        "target_mu_Ha": metadata.get("target_mu_Ha", ""),
        "initial_state": metadata.get("initial_state", ""),
        "source_job_id": metadata.get("source_job_id", ""),
        "water_orientation": metadata.get("water_orientation", ""),
        "chemistry_state": chemistry_state,
        "n_Pb": len(pb_indices),
        "n_O": len(o_indices),
        "n_H_total": len(h_indices),
        "n_water_H": len(water_h),
        "n_nonwater_H": len(nonwater_h),
        "water_H_counts_per_O": ";".join(str(count) for count in water_counts),
        "water_intact": water_intact,
        "OH_min_A": min(oh_distances) if oh_distances else "",
        "OH_max_A": max(oh_distances) if oh_distances else "",
        "HOH_angles_deg": ";".join(f"{angle:.3f}" for angle in hoh_angles),
        "PbH_min_A": min(pb_h_distances) if pb_h_distances else "",
        "PbH_max_A": max(pb_h_distances) if pb_h_distances else "",
        "nonwater_HH_A": nonwater_hh,
        "nonwater_H_zrel_min_A": min(pb_h_zrel) if pb_h_zrel else "",
        "nonwater_H_zrel_max_A": max(pb_h_zrel) if pb_h_zrel else "",
        "nonwater_H_nearest_Pb": ";".join(str(index) for index in nearest_pb_indices),
        "nonwater_H_same_Pb": same_pb if len(nearest_pb_indices) == 2 else "",
        "common_Pb_lift_A": common_pb_lift,
        "min_HH_all_A": min(all_hh) if all_hh else "",
        "H2_like_nonwater_H": h2_like,
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
        try:
            explicit_water_count = int(metadata.get("explicit_water_count") or 0)
        except (TypeError, ValueError):
            explicit_water_count = 0
        if explicit_water_count <= 0:
            continue
        row = analyze_job(metadata_path.parent, metadata, harvest)
        if row is not None:
            rows.append(row)

    rows.sort(key=lambda row: (float(row["target_mu_Ha"]) if row["target_mu_Ha"] not in ("", None) else 999.0,
                               row["job_id"]))
    if not rows:
        raise RuntimeError("No completed explicit-water Pb-H jobs found.")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print("Explicit-water Pb-H states")
    print("==========================")
    for row in rows:
        mu = format_float(row["target_mu_Ha"], digits=5)
        oh_min, oh_max = format_float(row["OH_min_A"]), format_float(row["OH_max_A"])
        pbh_min, pbh_max = format_float(row["PbH_min_A"]), format_float(row["PbH_max_A"])
        print(
            f"{row['job_id']:>4}  mu={mu:>8}  status={row['status']:<21}  "
            f"water={row['water_H_counts_per_O'] or 'NA':<5}  "
            f"OH={oh_min}-{oh_max} Å  PbH={pbh_min}-{pbh_max} Å  H2={row['H2_like_nonwater_H']}  "
            f"proton_well={row['proton_well_like_nonwater_H']}  {row['chemistry_state']}"
        )

    print(f"\nWrote: {OUTPUT}")


if __name__ == "__main__":
    main()
