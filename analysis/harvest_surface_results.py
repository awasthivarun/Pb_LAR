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

NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?"
FIRE_RE = re.compile(
    rf"FIRE:\s*(\d+)\s+\S+\s+({NUMBER})\s+({NUMBER})"
)


def parse_fmax_threshold(go_path):
    if not go_path.exists():
        return DEFAULT_FMAX

    text = go_path.read_text(errors="replace")

    matches = re.findall(rf"\bfmax\s*=\s*({NUMBER})", text)
    if matches:
        return float(matches[-1])

    return DEFAULT_FMAX


def parse_opt_log(path):
    if not path.exists():
        return None

    text = path.read_text(errors="replace")
    matches = FIRE_RE.findall(text)

    if not matches:
        return None

    step, energy, fmax = matches[-1]

    return {
        "fire_step": int(step),
        "ase_optimizer_energy_eV": float(energy),
        "final_fmax_eV_A": float(fmax),
    }


def latest_file(directory, names):
    candidates = []

    for name in names:
        p = directory / name
        if p.exists():
            candidates.append(p)

    if not candidates:
        return None

    return max(candidates, key=lambda p: p.stat().st_mtime)


def parse_jdftx(directory):
    # Search the persistent JDFTx output plus final Ecomponents if present.
    files = []

    out = directory / "out"
    if out.exists():
        files.append(out)

    files.extend(sorted(directory.glob("*Ecomponents*")))

    values = {
        "F_Ha": None,
        "G_Ha": None,
        "Etot_Ha": None,
        "muN_Ha": None,
        "nElectrons": None,
    }

    energy_patterns = {
        "F_Ha": re.compile(rf"(?m)^\s*F\s*=\s*({NUMBER})"),
        "G_Ha": re.compile(rf"(?m)^\s*G\s*=\s*({NUMBER})"),
        "Etot_Ha": re.compile(rf"(?m)^\s*Etot\s*=\s*({NUMBER})"),
        "muN_Ha": re.compile(rf"(?m)^\s*muN\s*=\s*({NUMBER})"),
    }

    n_patterns = [
        re.compile(rf"\bnElectrons\s*[:=]\s*({NUMBER})"),
        re.compile(rf"\bnElectrons\s+({NUMBER})"),
    ]

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

    # If JDFTx did not print G explicitly but did print F and muN,
    # use the JDFTx definition G = F - mu*N.
    if values["G_Ha"] is None and values["F_Ha"] is not None and values["muN_Ha"] is not None:
        values["G_Ha"] = values["F_Ha"] - values["muN_Ha"]

    for key in ("F_Ha", "G_Ha", "Etot_Ha", "muN_Ha"):
        if values[key] is not None:
            values[key.replace("_Ha", "_eV")] = values[key] * HA_TO_EV
        else:
            values[key.replace("_Ha", "_eV")] = None

    return values


def family_from_path(directory):
    rel = str(directory.relative_to(SURFACES))

    if "/PbH2_extraction/" in f"/{rel}/":
        return "PbH2_extraction"

    if "/fixed_mu/H_adsorption/" in f"/{rel}/":
        return "fixed_mu_1H"

    if "/fixed_mu/H2_candidates/" in f"/{rel}/":
        return "fixed_mu_2H"

    if "/H_subsurface/" in f"/{rel}/":
        return "subsurface_H"

    if "/H2_candidates/" in f"/{rel}/":
        return "neutral_2H"

    if "/H_adsorption/" in f"/{rel}/":
        return "neutral_1H"

    if "/defects/" in f"/{rel}/":
        return "defect"

    if "/convergence/" in f"/{rel}/":
        return "convergence"

    if "/fixed_mu/" in f"/{rel}/":
        return "fixed_mu_clean"

    if rel.endswith("/clean"):
        return "clean"

    return "other"


def geometry_metrics(path):
    if path is None or not path.exists():
        return {}

    atoms = read(path, format="vasp")
    symbols = np.array(atoms.get_chemical_symbols())

    pb = np.where(symbols == "Pb")[0]
    h = np.where(symbols == "H")[0]

    result = {
        "n_atoms_final": len(atoms),
        "n_Pb": len(pb),
        "n_H": len(h),
    }

    if len(pb):
        pb_z = atoms.positions[pb, 2]

        # All H-containing jobs currently have 36 Pb atoms, with 9 Pb per
        # ideal (111) layer. Median of the highest 9 Pb atoms remains a
        # stable surface reference even if one Pb begins to lift out.
        n_surface_reference = min(9, len(pb))
        top_z = np.sort(pb_z)[-n_surface_reference:]

        surface_z = float(np.median(top_z))

        result.update(
            {
                "surface_Pb_z_A": surface_z,
                "highest_Pb_z_A": float(np.max(pb_z)),
                "highest_Pb_lift_from_surface_A": float(np.max(pb_z) - surface_z),
                "top9_Pb_z_span_A": float(np.max(top_z) - np.min(top_z)),
            }
        )

    if len(h):
        heights = []
        nearest_distances = []
        nearest_pb_indices = []

        surface_z = result.get("surface_Pb_z_A", np.nan)

        for h_idx in h:
            heights.append(float(atoms.positions[h_idx, 2] - surface_z))

            distances = [
                atoms.get_distance(int(h_idx), int(pb_idx), mic=True)
                for pb_idx in pb
            ]

            nearest_local = int(np.argmin(distances))
            nearest_distances.append(float(distances[nearest_local]))
            nearest_pb_indices.append(int(pb[nearest_local]))

        result.update(
            {
                "H_height_min_A": float(np.min(heights)),
                "H_height_max_A": float(np.max(heights)),
                "PbH_distance_min_A": float(np.min(nearest_distances)),
                "PbH_distance_max_A": float(np.max(nearest_distances)),
                "H_nearest_Pb_indices": ";".join(map(str, nearest_pb_indices)),
            }
        )

        if len(h) == 2:
            result["HH_distance_A"] = float(
                atoms.get_distance(int(h[0]), int(h[1]), mic=True)
            )
            result["two_H_share_nearest_Pb"] = nearest_pb_indices[0] == nearest_pb_indices[1]

    return result


def clean_value(value):
    if isinstance(value, np.generic):
        return value.item()
    return value


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
    final_structure = contcar if contcar.exists() else None

    row = {
        "job_id": metadata.get("job_id"),
        "family": metadata.get("family") or family_from_path(directory),
        "state": metadata.get("state"),
        "source_job_id": metadata.get("source_job_id"),
        "source_path": metadata.get("source_path"),
        "directory": str(directory),
        "status": status,
        "purpose": metadata.get("purpose"),
        "target_mu_Ha": metadata.get("target_mu_Ha"),
        "approx_U_RHE_V_at_pH7": metadata.get("approx_U_RHE_V_at_pH7"),
        "fmax_threshold_eV_A": threshold,
    }

    if opt:
        row.update(opt)

    row.update(parse_jdftx(directory))
    row.update(geometry_metrics(final_structure))

    return {key: clean_value(value) for key, value in row.items()}


def print_ranked(rows, title, fixed_mu=False):
    rows = [r for r in rows if r["status"] == "CONVERGED"]

    if not rows:
        return

    print()
    print(title)
    print("-" * len(title))

    if fixed_mu:
        mus = sorted(
            {r["target_mu_Ha"] for r in rows if r["target_mu_Ha"] is not None}
        )

        for mu in mus:
            group = [r for r in rows if r["target_mu_Ha"] == mu]
            usable = [r for r in group if r.get("G_eV") is not None]

            print(f"\ntarget_mu = {mu:.4f} Ha")

            if not usable:
                print("  G unavailable in harvested outputs; no thermodynamic ranking made.")
                continue

            minimum = min(r["G_eV"] for r in usable)

            for r in sorted(usable, key=lambda x: x["G_eV"]):
                dE = r["G_eV"] - minimum
                print(
                    f"  {r['job_id']:>5}  "
                    f"G = {r['G_eV']: .6f} eV  "
                    f"dG = {dE: .4f} eV  "
                    f"Hheight = {r.get('H_height_min_A', float('nan')): .3f} A  "
                    f"Pb-H = {r.get('PbH_distance_min_A', float('nan')): .3f} A"
                )

    else:
        usable = [
            r for r in rows
            if r.get("ase_optimizer_energy_eV") is not None
        ]

        if not usable:
            return

        minimum = min(r["ase_optimizer_energy_eV"] for r in usable)

        for r in sorted(usable, key=lambda x: x["ase_optimizer_energy_eV"]):
            dE = r["ase_optimizer_energy_eV"] - minimum

            print(
                f"  {r['job_id']:>5}  "
                f"E = {r['ase_optimizer_energy_eV']: .6f} eV  "
                f"dE = {dE: .4f} eV  "
                f"Hheight = {r.get('H_height_min_A', float('nan')): .3f} A  "
                f"Pb-H = {r.get('PbH_distance_min_A', float('nan')): .3f} A"
            )


ANALYSIS.mkdir(parents=True, exist_ok=True)

metadata_files = sorted(SURFACES.rglob("metadata.json"))
rows = [harvest_job(path) for path in metadata_files]

fieldnames = sorted({key for row in rows for key in row})

with OUTPUT.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Scanned: {len(rows)} jobs")
print(f"Wrote:   {OUTPUT}")
print()

for status in ("CONVERGED", "INCOMPLETE_OR_RUNNING", "NO_OPT_RESULT"):
    print(f"{status:22s}: {sum(r['status'] == status for r in rows)}")

families = sorted({r["family"] for r in rows})

print()
print("Converged by family")
print("-------------------")
for family in families:
    n = sum(
        r["family"] == family and r["status"] == "CONVERGED"
        for r in rows
    )
    print(f"{family:20s} {n:3d}")


# These comparisons are valid because stoichiometry is identical within each group.
print_ranked(
    [r for r in rows if r["family"] == "neutral_1H"],
    "Neutral one-H site comparison",
)

print_ranked(
    [r for r in rows if r["family"] == "neutral_2H"],
    "Neutral two-H candidate comparison",
)

print_ranked(
    [r for r in rows if r["family"] == "fixed_mu_1H"],
    "Fixed-mu one-H comparison",
    fixed_mu=True,
)

print_ranked(
    [r for r in rows if r["family"] == "fixed_mu_2H"],
    "Fixed-mu two-H comparison",
    fixed_mu=True,
)

print()
print("No automatic energetic ranking is made between different stoichiometries.")
print("Defect formation, H adsorption, Pb extraction, and H2/PbH2 formation energies")
print("will be constructed explicitly from balanced reactions after harvesting.")