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

    if not matches:
        return None

    return float(matches[-1][2])


def classify_h(zrel, d_pb, pb_lift):
    if d_pb > 3.0:
        return "proton_well"

    if zrel < -0.30:
        return "subsurface_H"

    if pb_lift > 0.25 and d_pb < 2.4:
        return "lifted_PbH"

    return "surface_H"


rows = []

for meta_path in BASE.rglob("metadata.json"):
    directory = meta_path.parent
    contcar = directory / "CONTCAR"

    if not contcar.exists():
        continue

    atoms = read(contcar, format="vasp")
    symbols = np.array(atoms.get_chemical_symbols())

    pb_indices = np.where(symbols == "Pb")[0]
    h_indices = np.where(symbols == "H")[0]

    if len(h_indices) == 0:
        continue

    metadata = json.loads(meta_path.read_text())

    pb_z = atoms.positions[pb_indices, 2]

    # Pb(111) 3x3 slab: use the median height of the highest nine Pb atoms
    # as the reference top-layer height. This remains robust if one Pb lifts.
    surface_z = float(np.median(np.sort(pb_z)[-9:]))

    h_info = []

    for h_idx in h_indices:
        distances = np.array([
            atoms.get_distance(int(h_idx), int(pb_idx), mic=True)
            for pb_idx in pb_indices
        ])

        nearest_local = int(np.argmin(distances))
        nearest_pb = int(pb_indices[nearest_local])

        d_pb = float(distances[nearest_local])
        zrel = float(atoms.positions[h_idx, 2] - surface_z)
        pb_lift = float(atoms.positions[nearest_pb, 2] - surface_z)

        h_info.append({
            "state": classify_h(zrel, d_pb, pb_lift),
            "zrel": zrel,
            "dPb": d_pb,
            "Pb": nearest_pb,
            "PbLift": pb_lift,
        })

    hh_distance = None
    same_pb = None

    if len(h_indices) == 2:
        hh_distance = float(
            atoms.get_distance(
                int(h_indices[0]),
                int(h_indices[1]),
                mic=True,
            )
        )

        both_pb_bound = all(info["dPb"] < 3.0 for info in h_info)

        if both_pb_bound:
            same_pb = h_info[0]["Pb"] == h_info[1]["Pb"]

    rows.append({
        "job_id": str(metadata.get("job_id", "?")),
        "mu": metadata.get("target_mu_Ha"),
        "fmax": last_fmax(directory / "opt.log"),
        "h_info": h_info,
        "hh_distance": hh_distance,
        "same_pb": same_pb,
    })


lines = []

for row in sorted(rows, key=lambda x: x["job_id"]):
    mu = row["mu"]
    mu_str = "neutral" if mu is None else f"{mu:.4f}"

    fmax = row["fmax"]
    fmax_str = f"{fmax:.4f}" if fmax is not None else "---"

    parts = [
        f"{row['job_id']:5s}",
        f"mu={mu_str:>8s}",
        f"fmax={fmax_str}",
    ]

    for i, info in enumerate(row["h_info"], start=1):
        parts.append(
            f"H{i}={info['state']}"
            f"(z={info['zrel']:+.2f},"
            f"Pb-H={info['dPb']:.2f},"
            f"Pb#{info['Pb']},"
            f"PbLift={info['PbLift']:+.2f})"
        )

    if row["hh_distance"] is not None:
        parts.append(f"H-H={row['hh_distance']:.2f}")
        parts.append(f"samePb={row['same_pb']}")

    lines.append("  ".join(parts))


text = "\n".join(lines) + "\n"

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(text)

print(text, end="")
print(f"\nWrote: {OUTPUT}")