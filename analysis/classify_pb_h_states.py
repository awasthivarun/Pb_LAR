from pathlib import Path
import json
import re

import numpy as np
from ase.io import read


ROOT = Path("/pscratch/sd/a/awasthi/Pb_LAR")
BASE = ROOT / "surfaces/Pb111"
OUTPUT = ROOT / "analysis/pb_h_geometry_report.txt"

NUM = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?"
FIRE_RE = re.compile(rf"FIRE:\s*(\d+)\s+\S+\s+({NUM})\s+({NUM})")


def last_fmax(path):
    if not path.exists():
        return None
    matches = FIRE_RE.findall(path.read_text(errors="replace"))
    return float(matches[-1][2]) if matches else None


def classify_h(zrel, d_pb, pb_lift):
    if d_pb > 3.0:
        return "proton_well"
    if zrel < -0.30:
        return "subsurface_H"
    if pb_lift > 0.25 and d_pb < 2.4:
        return "lifted_PbH"
    return "surface_H"


def natural_key(job_id):
    return [int(token) if token.isdigit() else token for token in re.split(r"(\d+)", job_id)]


rows = []
skipped_explicit_water = []

for meta_path in BASE.rglob("metadata.json"):
    directory = meta_path.parent
    contcar = directory / "CONTCAR"
    if not contcar.is_file():
        continue

    atoms = read(contcar, format="vasp")
    atoms.set_pbc((True, True, False))
    symbols = np.array(atoms.get_chemical_symbols())

    pb_indices = np.where(symbols == "Pb")[0]
    o_indices = np.where(symbols == "O")[0]
    h_indices = np.where(symbols == "H")[0]
    if len(h_indices) == 0:
        continue

    metadata = json.loads(meta_path.read_text())
    job_id = str(metadata.get("job_id", "?"))

    # Explicit-water jobs are handled by analyze_explicit_water_states.py. Treating water H as Pb-H candidates
    # produces false proton-well assignments, so the general dry Pb/H classifier intentionally skips them.
    if len(o_indices) > 0:
        skipped_explicit_water.append(job_id)
        continue

    if len(pb_indices) == 0:
        raise ValueError(f"{job_id}: H-containing structure has no Pb atoms: {contcar}")

    pb_z = atoms.positions[pb_indices, 2]
    n_surface_reference = min(9, len(pb_indices))
    surface_z = float(np.median(np.sort(pb_z)[-n_surface_reference:]))
    h_info = []

    for h_idx in h_indices:
        distances = np.array([atoms.get_distance(int(h_idx), int(pb_idx), mic=True) for pb_idx in pb_indices])
        nearest_local = int(np.argmin(distances))
        nearest_pb = int(pb_indices[nearest_local])
        d_pb = float(distances[nearest_local])
        zrel = float(atoms.positions[h_idx, 2] - surface_z)
        pb_lift = float(atoms.positions[nearest_pb, 2] - surface_z)
        h_info.append({"state": classify_h(zrel, d_pb, pb_lift), "zrel": zrel, "dPb": d_pb,
                       "Pb": nearest_pb, "PbLift": pb_lift})

    hh_distance = None
    same_pb = None
    if len(h_indices) == 2:
        hh_distance = float(atoms.get_distance(int(h_indices[0]), int(h_indices[1]), mic=True))
        if all(info["dPb"] < 3.0 for info in h_info):
            same_pb = h_info[0]["Pb"] == h_info[1]["Pb"]

    rows.append({
        "job_id": job_id,
        "mu": metadata.get("target_mu_Ha"),
        "fmax": last_fmax(directory / "opt.log"),
        "h_info": h_info,
        "hh_distance": hh_distance,
        "same_pb": same_pb,
    })


lines = []
for row in sorted(rows, key=lambda item: natural_key(item["job_id"])):
    mu = row["mu"]
    mu_str = "neutral" if mu is None else f"{float(mu):.4f}"
    fmax = row["fmax"]
    fmax_str = f"{fmax:.4f}" if fmax is not None else "---"
    parts = [f"{row['job_id']:5s}", f"mu={mu_str:>8s}", f"fmax={fmax_str}"]

    for i, info in enumerate(row["h_info"], start=1):
        parts.append(
            f"H{i}={info['state']}(z={info['zrel']:+.2f},Pb-H={info['dPb']:.2f},"
            f"Pb#{info['Pb']},PbLift={info['PbLift']:+.2f})"
        )

    if row["hh_distance"] is not None:
        parts.extend([f"H-H={row['hh_distance']:.2f}", f"samePb={row['same_pb']}"])
    lines.append("  ".join(parts))

text = "\n".join(lines) + ("\n" if lines else "")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(text)

print(text, end="")
print(f"\nWrote: {OUTPUT}")
if skipped_explicit_water:
    print(f"Skipped {len(skipped_explicit_water)} explicit-water jobs; use analyze_explicit_water_states.py for those.")
