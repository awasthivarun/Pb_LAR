from pathlib import Path
import csv
import json
import re

import numpy as np
from ase.io import read


ROOT = Path("/pscratch/sd/a/awasthi/Pb_LAR")
SURFACES = ROOT / "surfaces"
ANALYSIS = ROOT / "analysis"
OUTPUT = ANALYSIS / "surface_results.csv"

HA_TO_EV = 27.211386245988
DEFAULT_FMAX = 0.04
OH_COVALENT_MAX_A = 1.25
PROTON_WELL_PBH_MIN_A = 3.0

NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?"
FIRE_RE = re.compile(rf"FIRE:\s*(\d+)\s+\S+\s+({NUMBER})\s+({NUMBER})")


def parse_fmax_threshold(go_path):
    if not go_path.exists():
        return DEFAULT_FMAX
    matches = re.findall(rf"\bfmax\s*=\s*({NUMBER})", go_path.read_text(errors="replace"))
    return float(matches[-1]) if matches else DEFAULT_FMAX


def parse_opt_log(path):
    if not path.exists():
        return None
    matches = FIRE_RE.findall(path.read_text(errors="replace"))
    if not matches:
        return None
    step, energy, fmax = matches[-1]
    return {"fire_step": int(step), "ase_optimizer_energy_eV": float(energy), "final_fmax_eV_A": float(fmax)}


def parse_jdftx(directory):
    # Search persistent JDFTx output plus Ecomponents dumps. Later files override earlier values.
    files = []
    out = directory / "out"
    if out.exists():
        files.append(out)
    files.extend(sorted(directory.glob("*Ecomponents*"), key=lambda path: path.stat().st_mtime))

    values = {"F_Ha": None, "G_Ha": None, "Etot_Ha": None, "muN_Ha": None, "nElectrons": None}
    energy_patterns = {
        "F_Ha": re.compile(rf"(?m)^\s*F\s*=\s*({NUMBER})"),
        "G_Ha": re.compile(rf"(?m)^\s*G\s*=\s*({NUMBER})"),
        "Etot_Ha": re.compile(rf"(?m)^\s*Etot\s*=\s*({NUMBER})"),
        "muN_Ha": re.compile(rf"(?m)^\s*muN\s*=\s*({NUMBER})"),
    }
    n_patterns = [re.compile(rf"\bnElectrons\s*[:=]\s*({NUMBER})"), re.compile(rf"\bnElectrons\s+({NUMBER})")]

    for path in files:
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        for key, pattern in energy_patterns.items():
            matches = pattern.findall(text)
            if matches:
                values[key] = float(matches[-1])
        for pattern in n_patterns:
            matches = pattern.findall(text)
            if matches:
                values["nElectrons"] = float(matches[-1])

    # JDFTx grand free energy definition used by this project: G = F - muN, where muN is the printed μN term.
    if values["G_Ha"] is None and values["F_Ha"] is not None and values["muN_Ha"] is not None:
        values["G_Ha"] = values["F_Ha"] - values["muN_Ha"]

    for key in ("F_Ha", "G_Ha", "Etot_Ha", "muN_Ha"):
        ev_key = key.replace("_Ha", "_eV")
        values[ev_key] = values[key] * HA_TO_EV if values[key] is not None else None
    return values


def family_from_path(directory):
    rel = str(directory.relative_to(SURFACES))
    wrapped = f"/{rel}/"
    if "/PbH2_extraction/explicit_water/" in wrapped:
        return "PbH2_extraction_explicit_water"
    if "/PbH2_extraction/" in wrapped:
        return "PbH2_extraction"
    if "/proton_well_rescue/" in wrapped:
        return "proton_well_rescue"
    if "/fixed_mu/H_adsorption/" in wrapped:
        return "fixed_mu_1H"
    if "/fixed_mu/H2_candidates/" in wrapped or "/fixed_mu/H2_reference/" in wrapped:
        return "fixed_mu_2H"
    if "/H_subsurface/" in wrapped:
        return "subsurface_H"
    if "/H2_candidates/" in wrapped:
        return "neutral_2H"
    if "/H_adsorption/" in wrapped:
        return "neutral_1H"
    if "/defects/" in wrapped:
        return "defect"
    if "/convergence/" in wrapped:
        return "convergence"
    if "/fixed_mu/" in wrapped:
        return "fixed_mu_clean"
    if rel.endswith("/clean"):
        return "clean"
    return "other"


def geometry_metrics(path):
    if path is None or not path.exists():
        return {}

    atoms = read(path, format="vasp")
    atoms.set_pbc((True, True, False))
    symbols = np.array(atoms.get_chemical_symbols())
    pb = np.where(symbols == "Pb")[0]
    o = np.where(symbols == "O")[0]
    h = np.where(symbols == "H")[0]
    result = {"n_atoms_final": len(atoms), "n_Pb": len(pb), "n_O": len(o), "n_H": len(h)}

    if len(pb):
        pb_z = atoms.positions[pb, 2]
        n_surface_reference = min(9, len(pb))
        top_z = np.sort(pb_z)[-n_surface_reference:]
        surface_z = float(np.median(top_z))
        result.update({
            "surface_Pb_z_A": surface_z,
            "highest_Pb_z_A": float(np.max(pb_z)),
            "highest_Pb_lift_from_surface_A": float(np.max(pb_z) - surface_z),
            "top9_Pb_z_span_A": float(np.max(top_z) - np.min(top_z)),
        })

    if not len(h) or not len(pb):
        return result

    water_h = set()
    if len(o):
        for h_idx in h:
            nearest_o = min(atoms.get_distance(int(h_idx), int(o_idx), mic=True) for o_idx in o)
            if nearest_o <= OH_COVALENT_MAX_A:
                water_h.add(int(h_idx))

    relevant_h = [int(h_idx) for h_idx in h if int(h_idx) not in water_h]
    result["n_water_H"] = len(water_h)
    result["n_nonwater_H"] = len(relevant_h)
    if not relevant_h:
        return result

    surface_z = result.get("surface_Pb_z_A", np.nan)
    heights = []
    nearest_distances = []
    nearest_pb_indices = []
    for h_idx in relevant_h:
        heights.append(float(atoms.positions[h_idx, 2] - surface_z))
        distances = np.array([atoms.get_distance(h_idx, int(pb_idx), mic=True) for pb_idx in pb])
        nearest_local = int(np.argmin(distances))
        nearest_distances.append(float(distances[nearest_local]))
        nearest_pb_indices.append(int(pb[nearest_local]))

    result.update({
        "H_height_min_A": float(np.min(heights)),
        "H_height_max_A": float(np.max(heights)),
        "PbH_distance_min_A": float(np.min(nearest_distances)),
        "PbH_distance_max_A": float(np.max(nearest_distances)),
        "H_nearest_Pb_indices": ";".join(map(str, nearest_pb_indices)),
    })

    if len(relevant_h) == 2:
        result["HH_distance_A"] = float(atoms.get_distance(relevant_h[0], relevant_h[1], mic=True))
        result["two_H_share_nearest_Pb"] = nearest_pb_indices[0] == nearest_pb_indices[1]
    return result


def clean_value(value):
    return value.item() if isinstance(value, np.generic) else value


def harvest_job(metadata_path):
    directory = metadata_path.parent
    metadata = json.loads(metadata_path.read_text())
    opt = parse_opt_log(directory / "opt.log")
    threshold = parse_fmax_threshold(directory / "go.py")

    if opt is None:
        status = "NO_OPT_RESULT"
    elif opt["final_fmax_eV_A"] <= threshold:
        status = "CONVERGED"
    else:
        status = "INCOMPLETE_OR_RUNNING"

    contcar = directory / "CONTCAR"
    row = {
        "job_id": metadata.get("job_id"),
        "family": metadata.get("family") or family_from_path(directory),
        "state": metadata.get("state"),
        "initial_state": metadata.get("initial_state"),
        "state_label_scope": metadata.get("state_label_scope"),
        "source_job_id": metadata.get("source_job_id"),
        "source_path": metadata.get("source_path"),
        "directory": str(directory),
        "status": status,
        "purpose": metadata.get("purpose"),
        "target_mu_Ha": metadata.get("target_mu_Ha"),
        "approx_U_RHE_V_at_pH7": metadata.get("approx_U_RHE_V_at_pH7"),
        "explicit_water_count": metadata.get("explicit_water_count"),
        "water_orientation": metadata.get("water_orientation"),
        "fmax_threshold_eV_A": threshold,
    }
    if opt:
        row.update(opt)
    row.update(parse_jdftx(directory))
    row.update(geometry_metrics(contcar if contcar.exists() else None))
    return {key: clean_value(value) for key, value in row.items()}


def leaves_surface_bound_H_family(row):
    max_pbh = row.get("PbH_distance_max_A")
    return max_pbh is not None and float(max_pbh) > PROTON_WELL_PBH_MIN_A


def print_ranked(rows, title, fixed_mu=False):
    converged = [row for row in rows if row["status"] == "CONVERGED"]
    if not converged:
        return

    excluded = [row for row in converged if fixed_mu and leaves_surface_bound_H_family(row)]
    rows = [row for row in converged if row not in excluded]

    print()
    print(title)
    print("-" * len(title))
    if excluded:
        print("Excluded non-surface-bound (>3 Å Pb-H) geometries from automatic ranking: " + ", ".join(row["job_id"] for row in excluded))
    if not rows:
        print("No physical-looking converged structures remain for automatic ranking.")
        return

    if fixed_mu:
        mus = sorted({row["target_mu_Ha"] for row in rows if row["target_mu_Ha"] is not None})
        for mu in mus:
            group = [row for row in rows if row["target_mu_Ha"] == mu]
            usable = [row for row in group if row.get("G_eV") is not None]
            print(f"\ntarget_mu = {mu:.5f} Ha")
            if not usable:
                print("  G unavailable in harvested outputs; no thermodynamic ranking made.")
                continue
            minimum = min(row["G_eV"] for row in usable)
            for row in sorted(usable, key=lambda item: item["G_eV"]):
                print(
                    f"  {row['job_id']:>5}  G = {row['G_eV']: .6f} eV  dG = {row['G_eV'] - minimum: .4f} eV  "
                    f"Hheight = {row.get('H_height_min_A', float('nan')): .3f} Å  "
                    f"Pb-H = {row.get('PbH_distance_min_A', float('nan')): .3f} Å"
                )
    else:
        usable = [row for row in rows if row.get("ase_optimizer_energy_eV") is not None]
        if not usable:
            return
        minimum = min(row["ase_optimizer_energy_eV"] for row in usable)
        for row in sorted(usable, key=lambda item: item["ase_optimizer_energy_eV"]):
            print(
                f"  {row['job_id']:>5}  E = {row['ase_optimizer_energy_eV']: .6f} eV  "
                f"dE = {row['ase_optimizer_energy_eV'] - minimum: .4f} eV  "
                f"Hheight = {row.get('H_height_min_A', float('nan')): .3f} Å  "
                f"Pb-H = {row.get('PbH_distance_min_A', float('nan')): .3f} Å"
            )


ANALYSIS.mkdir(parents=True, exist_ok=True)
metadata_files = sorted(SURFACES.rglob("metadata.json")) if SURFACES.exists() else []
rows = [harvest_job(path) for path in metadata_files]
if not rows:
    raise RuntimeError(f"No surface metadata.json files found under {SURFACES}")

fieldnames = sorted({key for row in rows for key in row})
with OUTPUT.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Scanned: {len(rows)} jobs")
print(f"Wrote:   {OUTPUT}")
print()
for status in ("CONVERGED", "INCOMPLETE_OR_RUNNING", "NO_OPT_RESULT"):
    print(f"{status:22s}: {sum(row['status'] == status for row in rows)}")

families = sorted({row["family"] for row in rows})
print("\nConverged by family\n-------------------")
for family in families:
    n_converged = sum(row["family"] == family and row["status"] == "CONVERGED" for row in rows)
    print(f"{family:32s} {n_converged:3d}")

# These automatic rankings are only made within equal-stoichiometry families.
print_ranked([row for row in rows if row["family"] == "neutral_1H"], "Neutral one-H site comparison")
print_ranked([row for row in rows if row["family"] == "neutral_2H"], "Neutral two-H candidate comparison")
print_ranked([row for row in rows if row["family"] == "fixed_mu_1H"], "Fixed-mu one-H comparison", fixed_mu=True)
print_ranked([row for row in rows if row["family"] == "fixed_mu_2H"], "Fixed-mu two-H comparison", fixed_mu=True)

print("\nNo automatic energetic ranking is made between different stoichiometries or specialized extraction families.")
print("Defect formation, H adsorption, Pb extraction, hydrated detachment, and H2/PbH2 reaction energies must be")
print("constructed explicitly from balanced reactions after harvesting and geometry classification.")
