from pathlib import Path
import csv
import json
import re

import matplotlib.pyplot as plt
import numpy as np
from ase.io import read


ROOT = Path("/pscratch/sd/a/awasthi/Pb_LAR")
SURFACE_RESULTS = ROOT / "analysis/surface_results.csv"

JOBS = {
    "X10_dry_proton_well": {
        "job_id": "X10",
        "directory": ROOT / "surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p09725",
        "role": "dry_proton_well",
    },
    "X22_hydrated_rescue": {
        "job_id": "X22",
        "directory": ROOT / "surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p09725",
        "role": "hydrated_rescue",
    },
}

TARGET_MU_HA = -0.09725
OH_COVALENT_MAX_A = 1.25
BOUND_PBH_MAX_A = 2.60
PROTON_WELL_PBH_MIN_A = 3.00

OUTDIR = ROOT / "analysis/proton_well_diagnostics"
EXPECTED_OUTPUTS = [
    OUTDIR / "01_cavity_shape.png",
    OUTDIR / "02_electron_density_with_cavity.png",
    OUTDIR / "03_bound_charge_with_cavity.png",
    OUTDIR / "04_dielectric_response_with_cavity.png",
    OUTDIR / "05_ionic_response_with_cavity.png",
    OUTDIR / "06_outward_profiles.png",
    OUTDIR / "point_metrics.csv",
    OUTDIR / "outward_profiles.csv",
]

FIELD_FILES = {
    "n": "job.n",
    "shape": "job.fluidShape",
    "nbound": "job.nbound",
    "rho_diel": "job.fluidRhoDiel",
    "rho_ion": "job.fluidRhoIon",
    "vfluid": "job.V_fluidTot",
}


def unit(vector):
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    if norm < 1e-12:
        raise ValueError("Cannot normalize a near-zero vector.")
    return vector / norm


def cart_to_frac(points, cell):
    return np.asarray(points, dtype=float) @ np.linalg.inv(np.asarray(cell, dtype=float))


def load_harvest():
    if not SURFACE_RESULTS.is_file():
        raise FileNotFoundError(f"Missing harvested results: {SURFACE_RESULTS}")

    rows = {}
    with SURFACE_RESULTS.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["job_id"]] = row
    return rows


def parse_fftbox(out_path, n_values):
    candidates = []
    lines = out_path.read_text(errors="replace").splitlines()

    for line in lines:
        if "Chosen fftbox size" not in line:
            continue
        numbers = [int(x) for x in re.findall(r"\d+", line)]
        for i in range(max(0, len(numbers) - 2)):
            shape = tuple(numbers[i:i + 3])
            if len(shape) == 3 and np.prod(shape) == n_values:
                candidates.append(shape)

    candidates = list(dict.fromkeys(candidates))
    if len(candidates) != 1:
        relevant = [line for line in lines if "Chosen fftbox size" in line]
        raise RuntimeError(
            f"Could not uniquely identify FFT grid from {out_path}.\n"
            f"Electron-density values: {n_values}\nCandidates: {candidates}\n" + "\n".join(relevant)
        )
    return candidates[0]


def load_raw_field(path, normal_shape):
    raw = np.fromfile(path, dtype="<f8")
    n_normal = int(np.prod(normal_shape))

    if raw.size == n_normal:
        return raw.reshape(normal_shape), "normal"

    doubled_z_shape = (normal_shape[0], normal_shape[1], 2 * normal_shape[2])
    if raw.size == 2 * n_normal:
        return raw.reshape(doubled_z_shape), "double_z"

    raise ValueError(f"{path} contains {raw.size} doubles; expected {n_normal} or {2 * n_normal}.")


def trilinear(array, coordinates):
    coordinates = np.asarray(coordinates, dtype=float)
    i0 = np.floor(coordinates).astype(int)
    frac = coordinates - np.floor(coordinates)
    i1 = i0 + 1

    # JDFTx field files are FFT-grid objects, so interpolation is periodic on the stored grid.
    for axis, size in enumerate(array.shape):
        i0[:, axis] %= size
        i1[:, axis] %= size

    x, y, z = frac[:, 0], frac[:, 1], frac[:, 2]
    c000 = array[i0[:, 0], i0[:, 1], i0[:, 2]]
    c001 = array[i0[:, 0], i0[:, 1], i1[:, 2]]
    c010 = array[i0[:, 0], i1[:, 1], i0[:, 2]]
    c011 = array[i0[:, 0], i1[:, 1], i1[:, 2]]
    c100 = array[i1[:, 0], i0[:, 1], i0[:, 2]]
    c101 = array[i1[:, 0], i0[:, 1], i1[:, 2]]
    c110 = array[i1[:, 0], i1[:, 1], i0[:, 2]]
    c111 = array[i1[:, 0], i1[:, 1], i1[:, 2]]

    c00 = c000 * (1.0 - z) + c001 * z
    c01 = c010 * (1.0 - z) + c011 * z
    c10 = c100 * (1.0 - z) + c101 * z
    c11 = c110 * (1.0 - z) + c111 * z
    c0 = c00 * (1.0 - y) + c01 * y
    c1 = c10 * (1.0 - y) + c11 * y
    return c0 * (1.0 - x) + c1 * x


def identify_relevant_h(atoms, role):
    symbols = np.array(atoms.get_chemical_symbols())
    pb_indices = np.where(symbols == "Pb")[0]
    o_indices = np.where(symbols == "O")[0]
    h_indices = np.where(symbols == "H")[0]

    if len(pb_indices) != 36:
        raise ValueError(f"Expected 36 Pb atoms, found {len(pb_indices)}.")

    nearest_o = {}
    water_h = set()
    if len(o_indices):
        for h_idx in h_indices:
            distances = np.array([atoms.get_distance(int(h_idx), int(o_idx), mic=True) for o_idx in o_indices])
            local = int(np.argmin(distances))
            nearest_o[int(h_idx)] = (int(o_indices[local]), float(distances[local]))
            if distances[local] <= OH_COVALENT_MAX_A:
                water_h.add(int(h_idx))

    active_h = [int(h_idx) for h_idx in h_indices if int(h_idx) not in water_h]
    if len(active_h) != 2:
        raise ValueError(f"Expected exactly two non-water H atoms; found {active_h}.")

    if role == "dry_proton_well":
        if len(o_indices) != 0 or len(h_indices) != 2:
            raise ValueError(f"Dry proton-well reference should be Pb36H2; found O={len(o_indices)}, H={len(h_indices)}.")
    elif role == "hydrated_rescue":
        if len(o_indices) != 2 or len(h_indices) != 6:
            raise ValueError(f"Hydrated rescue should be Pb36O2H6; found O={len(o_indices)}, H={len(h_indices)}.")
        counts = []
        for o_idx in o_indices:
            counts.append(sum(1 for h_idx in water_h if nearest_o[h_idx][0] == int(o_idx)))
        if counts != [2, 2]:
            raise ValueError(f"Hydrated rescue does not contain two intact H2O molecules: H counts per O = {counts}.")
    else:
        raise ValueError(f"Unknown comparison role: {role}")

    nearest_pb = []
    pb_h_distances = []
    for h_idx in active_h:
        distances = np.array([atoms.get_distance(h_idx, int(pb_idx), mic=True) for pb_idx in pb_indices])
        local = int(np.argmin(distances))
        nearest_pb.append(int(pb_indices[local]))
        pb_h_distances.append(float(distances[local]))

    if nearest_pb[0] != nearest_pb[1]:
        raise ValueError(f"The two relevant H atoms do not share one Pb: {nearest_pb}")

    if role == "dry_proton_well" and min(pb_h_distances) <= PROTON_WELL_PBH_MIN_A:
        raise ValueError(f"X10 no longer looks like a proton well: Pb-H = {pb_h_distances}")
    if role == "hydrated_rescue" and max(pb_h_distances) >= BOUND_PBH_MAX_A:
        raise ValueError(f"X22 no longer looks like bound Pb(H)2: Pb-H = {pb_h_distances}")

    return nearest_pb[0], active_h, water_h, pb_h_distances


def validate_job_metadata(name, spec, harvest):
    job_id = spec["job_id"]
    directory = spec["directory"]
    metadata_path = directory / "metadata.json"
    contcar_path = directory / "CONTCAR"

    if job_id not in harvest:
        raise KeyError(f"{job_id} is missing from {SURFACE_RESULTS}.")
    if harvest[job_id].get("status") != "CONVERGED":
        raise RuntimeError(f"{job_id} is not converged: status={harvest[job_id].get('status')}")
    if not metadata_path.is_file():
        raise FileNotFoundError(metadata_path)
    if not contcar_path.is_file():
        raise FileNotFoundError(contcar_path)

    metadata = json.loads(metadata_path.read_text())
    if metadata.get("job_id") != job_id:
        raise ValueError(f"{metadata_path} identifies {metadata.get('job_id')}, expected {job_id}.")
    mu = metadata.get("target_mu_Ha")
    if mu is None or not np.isclose(float(mu), TARGET_MU_HA, atol=1e-8, rtol=0.0):
        raise ValueError(f"{job_id} target-mu is {mu}; expected {TARGET_MU_HA} Ha.")

    atoms = read(contcar_path, format="vasp")
    atoms.set_pbc((True, True, False))
    central_pb, active_h, water_h, pb_h_distances = identify_relevant_h(atoms, spec["role"])

    return {
        "name": name,
        "job_id": job_id,
        "role": spec["role"],
        "directory": directory,
        "metadata": metadata,
        "atoms": atoms,
        "central_pb": central_pb,
        "active_h": active_h,
        "water_h": water_h,
        "PbH_distances_A": pb_h_distances,
    }


def sample_fractional_on_fluid(array, frac, normal_shape, z_sign, z_offset):
    frac = np.asarray(frac, dtype=float).copy()
    frac[:, 0] %= 1.0
    frac[:, 1] %= 1.0

    coords = np.empty_like(frac)
    coords[:, 0] = frac[:, 0] * normal_shape[0]
    coords[:, 1] = frac[:, 1] * normal_shape[1]
    coords[:, 2] = z_sign * frac[:, 2] * normal_shape[2] + z_offset
    return trilinear(array, coords)


def infer_fluid_z_mapping(atoms, shape_field, normal_shape, central_pb):
    symbols = np.array(atoms.get_chemical_symbols())
    low_indices = [i for i, symbol in enumerate(symbols) if symbol in {"Pb", "O"}]
    low_frac = cart_to_frac(atoms.positions[low_indices], atoms.cell)

    pb_indices = np.where(symbols == "Pb")[0]
    pb_z = atoms.positions[pb_indices, 2]
    top_z = float(np.max(pb_z))
    bottom_z = float(np.min(pb_z))
    cell_z = float(atoms.cell[2, 2])
    pb_xy = atoms.positions[central_pb, :2]

    vacuum_cart = np.array([
        [pb_xy[0], pb_xy[1], min(top_z + 6.0, cell_z - 1.0)],
        [pb_xy[0], pb_xy[1], max(bottom_z - 6.0, 1.0)],
    ])
    vacuum_frac = cart_to_frac(vacuum_cart, atoms.cell)

    def evaluate(sign, offset):
        low_values = sample_fractional_on_fluid(shape_field, low_frac, normal_shape, sign, offset)
        vacuum_values = sample_fractional_on_fluid(shape_field, vacuum_frac, normal_shape, sign, offset)
        score = np.mean(low_values**2) + 0.5 * np.mean((vacuum_values - 1.0)**2)
        return float(score), low_values, vacuum_values

    if shape_field.shape == tuple(normal_shape):
        score, low_values, vacuum_values = evaluate(1.0, 0.0)
        best = (score, 1.0, 0.0, low_values, vacuum_values)
    else:
        expected = (normal_shape[0], normal_shape[1], 2 * normal_shape[2])
        if shape_field.shape != expected:
            raise ValueError(f"Unexpected fluid grid {shape_field.shape}; expected {normal_shape} or {expected}.")

        best = None
        for sign in (1.0, -1.0):
            for offset in np.arange(0.0, 2.0 * normal_shape[2], 1.0):
                score, low_values, vacuum_values = evaluate(sign, offset)
                if best is None or score < best[0]:
                    best = (score, sign, float(offset), low_values, vacuum_values)

        _, best_sign, best_offset, _, _ = best
        for offset in np.arange(best_offset - 1.0, best_offset + 1.0001, 0.05):
            score, low_values, vacuum_values = evaluate(best_sign, offset)
            if score < best[0]:
                best = (score, best_sign, float(offset), low_values, vacuum_values)

    score, sign, offset, low_values, vacuum_values = best
    diagnostics = {
        "score": score,
        "mean_shape_explicit_atoms": float(np.mean(low_values)),
        "max_shape_explicit_atoms": float(np.max(low_values)),
        "mean_shape_vacuum": float(np.mean(vacuum_values)),
        "vacuum_values": vacuum_values.tolist(),
    }

    if diagnostics["mean_shape_explicit_atoms"] > 0.25:
        raise RuntimeError(
            "Could not find a convincing fluid-grid alignment: "
            f"mean shape at Pb/O = {diagnostics['mean_shape_explicit_atoms']:.3f}"
        )
    if diagnostics["mean_shape_vacuum"] < 0.70:
        raise RuntimeError(
            "Could not find a convincing fluid-grid alignment: "
            f"mean vacuum shape = {diagnostics['mean_shape_vacuum']:.3f}"
        )

    return sign, offset, diagnostics


def load_job(validated):
    directory = validated["directory"]
    atoms = validated["atoms"]
    n_path = directory / FIELD_FILES["n"]
    out_path = directory / "out"

    if not n_path.is_file():
        raise FileNotFoundError(n_path)
    if not out_path.is_file():
        raise FileNotFoundError(out_path)

    n_values = n_path.stat().st_size // 8
    normal_shape = parse_fftbox(out_path, n_values)
    fields = {}
    field_modes = {}

    for key, filename in FIELD_FILES.items():
        path = directory / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        fields[key], field_modes[key] = load_raw_field(path, normal_shape)

    fluid_sign, fluid_offset, fluid_diagnostics = infer_fluid_z_mapping(
        atoms, fields["shape"], normal_shape, validated["central_pb"]
    )

    return {
        **validated,
        "normal_shape": normal_shape,
        "fields": fields,
        "field_modes": field_modes,
        "fluid_sign": fluid_sign,
        "fluid_offset": fluid_offset,
        "fluid_diagnostics": fluid_diagnostics,
    }


def validate_physical_fractional_z(frac, context):
    z = np.asarray(frac)[:, 2]
    if np.min(z) < -1e-8 or np.max(z) > 1.0 + 1e-8:
        raise ValueError(
            f"{context} leaves the physical z cell: fractional z range = [{np.min(z):.6f}, {np.max(z):.6f}]."
        )


def sample_job_field(job, field_key, cart_points):
    cart_points = np.asarray(cart_points, dtype=float)
    original_shape = cart_points.shape[:-1]
    points = cart_points.reshape(-1, 3)
    frac = cart_to_frac(points, job["atoms"].cell)
    validate_physical_fractional_z(frac, f"{job['name']} {field_key} sampling")

    frac[:, 0] %= 1.0
    frac[:, 1] %= 1.0
    frac[:, 2] = np.clip(frac[:, 2], 0.0, np.nextafter(1.0, 0.0))

    field = job["fields"][field_key]
    mode = job["field_modes"][field_key]
    normal_shape = job["normal_shape"]

    if mode == "normal":
        coords = frac * np.asarray(normal_shape, dtype=float)
        values = trilinear(field, coords)
    elif mode == "double_z":
        values = sample_fractional_on_fluid(field, frac, normal_shape, job["fluid_sign"], job["fluid_offset"])
    else:
        raise ValueError(mode)

    return values.reshape(original_shape)


def minimum_image_vector(origin, position, cell):
    frac = cart_to_frac(np.asarray(position) - np.asarray(origin), cell)
    frac[0] -= np.round(frac[0])
    frac[1] -= np.round(frac[1])
    return frac @ np.asarray(cell)


def make_plane_basis(job):
    atoms = job["atoms"]
    pb_idx = job["central_pb"]
    h1, h2 = job["active_h"]
    origin = atoms.positions[pb_idx].copy()
    v1 = atoms.get_distance(pb_idx, h1, mic=True, vector=True)
    v2 = atoms.get_distance(pb_idx, h2, mic=True, vector=True)

    e_u = unit(v2 - v1)
    midpoint_vector = 0.5 * (v1 + v2)
    e_v = unit(midpoint_vector - np.dot(midpoint_vector, e_u) * e_u)
    if e_v[2] < 0.0:
        e_v *= -1.0
    e_normal = unit(np.cross(e_u, e_v))
    return origin, e_u, e_v, e_normal


def build_plane(job):
    origin, e_u, e_v, e_normal = make_plane_basis(job)
    u = np.linspace(-4.5, 4.5, 361)
    v = np.linspace(-2.5, 7.0, 381)
    U, V = np.meshgrid(u, v, indexing="xy")
    points = origin[None, None, :] + U[:, :, None] * e_u[None, None, :] + V[:, :, None] * e_v[None, None, :]
    slices = {key: sample_job_field(job, key, points) for key in FIELD_FILES}
    return {
        "origin": origin,
        "e_u": e_u,
        "e_v": e_v,
        "e_normal": e_normal,
        "u": u,
        "v": v,
        "U": U,
        "V": V,
        "slices": slices,
    }


def overlay_atoms(ax, job, plane):
    atoms = job["atoms"]
    origin = plane["origin"]
    e_u = plane["e_u"]
    e_v = plane["e_v"]
    e_normal = plane["e_normal"]
    projected = []

    for idx, (symbol, position) in enumerate(zip(atoms.get_chemical_symbols(), atoms.positions)):
        dr = minimum_image_vector(origin, position, atoms.cell)
        u = float(np.dot(dr, e_u))
        v = float(np.dot(dr, e_v))
        out_of_plane = abs(float(np.dot(dr, e_normal)))
        if out_of_plane <= 0.75 and -4.8 <= u <= 4.8 and -2.8 <= v <= 7.3:
            projected.append((idx, symbol, u, v))

    styles = {
        "Pb": dict(s=42, marker="o", facecolor="0.65", edgecolor="0.25"),
        "O": dict(s=52, marker="o", facecolor="tab:red", edgecolor="black"),
        "H": dict(s=38, marker="o", facecolor="white", edgecolor="black"),
    }

    for symbol in ["Pb", "O", "H"]:
        subset = [item for item in projected if item[1] == symbol]
        if subset:
            ax.scatter(
                [item[2] for item in subset], [item[3] for item in subset], linewidths=0.6, zorder=6, **styles[symbol]
            )

    for idx, _, u, v in projected:
        if idx == job["central_pb"]:
            ax.scatter([u], [v], s=90, marker="s", facecolor="none", edgecolor="black", linewidths=1.4, zorder=7)
        if idx in job["active_h"]:
            ax.scatter([u], [v], s=90, marker="*", facecolor="none", edgecolor="black", linewidths=1.2, zorder=7)


def plot_pair(jobs, planes, field_key, filename, label, transform=None, symmetric=False):
    arrays = []
    for job in jobs:
        data = planes[job["name"]]["slices"][field_key]
        arrays.append(transform(data) if transform is not None else data)

    if symmetric:
        concatenated = np.concatenate([np.abs(array[np.isfinite(array)]).ravel() for array in arrays])
        vmax = float(np.quantile(concatenated, 0.995))
        vmax = vmax if vmax > 0.0 else 1.0
        vmin, cmap = -vmax, "RdBu_r"
    else:
        concatenated = np.concatenate([array[np.isfinite(array)].ravel() for array in arrays])
        vmin = float(np.quantile(concatenated, 0.01))
        vmax = float(np.quantile(concatenated, 0.995))
        cmap = "viridis"

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), constrained_layout=True)
    image = None
    for ax, job, data in zip(axes, jobs, arrays):
        plane = planes[job["name"]]
        image = ax.imshow(
            data,
            origin="lower",
            extent=[plane["u"][0], plane["u"][-1], plane["v"][0], plane["v"][-1]],
            aspect="equal",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
        )
        if field_key != "shape":
            ax.contour(plane["U"], plane["V"], plane["slices"]["shape"], levels=[0.5], linewidths=[1.5], colors=["black"])
        overlay_atoms(ax, job, plane)
        ax.set_title(job["name"])
        ax.set_xlabel("H-H direction / Å")
        ax.set_ylabel("Pb -> H midpoint direction / Å")

    fig.colorbar(image, ax=axes, label=label, shrink=0.88)
    fig.savefig(OUTDIR / filename, dpi=220)
    plt.close(fig)


def write_csv(path, rows):
    if not rows:
        raise RuntimeError(f"No rows available for {path.name}.")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    existing = [path for path in EXPECTED_OUTPUTS if path.exists()]
    if existing:
        raise FileExistsError(
            "Refusing to overwrite existing proton-well diagnostics:\n" + "\n".join(str(path) for path in existing)
        )

    harvest = load_harvest()
    validated = [validate_job_metadata(name, spec, harvest) for name, spec in JOBS.items()]
    if not np.allclose(validated[0]["atoms"].cell.array, validated[1]["atoms"].cell.array, atol=1e-8, rtol=0.0):
        raise ValueError("X10 and X22 use different simulation cells; direct spatial field comparison is not valid.")

    jobs = [load_job(item) for item in validated]
    OUTDIR.mkdir(parents=True, exist_ok=True)
    planes = {job["name"]: build_plane(job) for job in jobs}

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), constrained_layout=True)
    image = None
    for ax, job in zip(axes, jobs):
        plane = planes[job["name"]]
        shape = plane["slices"]["shape"]
        image = ax.imshow(
            shape,
            origin="lower",
            extent=[plane["u"][0], plane["u"][-1], plane["v"][0], plane["v"][-1]],
            aspect="equal",
            cmap="viridis",
            vmin=0.0,
            vmax=1.0,
        )
        ax.contour(
            plane["U"], plane["V"], shape, levels=[0.1, 0.5, 0.9], colors=["black"] * 3,
            linewidths=[0.6, 1.6, 0.6], linestyles=["dotted", "solid", "dashed"],
        )
        overlay_atoms(ax, job, plane)
        ax.set_title(job["name"])
        ax.set_xlabel("H-H direction / Å")
        ax.set_ylabel("Pb -> H midpoint direction / Å")

    fig.colorbar(image, ax=axes, label="fluidShape: 0 = solute/cavity, 1 = bulk fluid", shrink=0.88)
    fig.savefig(OUTDIR / "01_cavity_shape.png", dpi=220)
    plt.close(fig)

    plot_pair(
        jobs, planes, "n", "02_electron_density_with_cavity.png", r"log10 electron density [e / bohr$^3$]",
        transform=lambda x: np.log10(np.clip(x, 1e-10, None)),
    )
    plot_pair(jobs, planes, "nbound", "03_bound_charge_with_cavity.png", "BoundCharge [JDFTx raw density units]", symmetric=True)
    plot_pair(
        jobs, planes, "rho_diel", "04_dielectric_response_with_cavity.png",
        "fluidRhoDiel [JDFTx raw density units]", symmetric=True,
    )
    plot_pair(
        jobs, planes, "rho_ion", "05_ionic_response_with_cavity.png",
        "fluidRhoIon [JDFTx raw density units]", symmetric=True,
    )

    metric_rows = []
    profile_rows = []
    profiles_for_plot = {}

    for job in jobs:
        atoms = job["atoms"]
        pb_idx = job["central_pb"]
        individual_profiles = []

        for local_h_number, h_idx in enumerate(job["active_h"], start=1):
            h_position = atoms.positions[h_idx].copy()
            pb_to_h = atoms.get_distance(pb_idx, h_idx, mic=True, vector=True)
            pb_h_distance = float(np.linalg.norm(pb_to_h))
            outward = unit(pb_to_h)
            point = h_position[None, :]
            values_at_h = {key: float(sample_job_field(job, key, point)[0]) for key in FIELD_FILES}

            t = np.linspace(0.0, 4.0, 401)
            line_points = h_position[None, :] + t[:, None] * outward[None, :]
            line = {key: sample_job_field(job, key, line_points) for key in FIELD_FILES}
            shape_line = line["shape"]

            if shape_line[0] >= 0.5:
                cavity_clearance = 0.0
            else:
                crossings = np.where((shape_line[:-1] < 0.5) & (shape_line[1:] >= 0.5))[0]
                if len(crossings):
                    i = int(crossings[0])
                    x0, x1 = t[i], t[i + 1]
                    y0, y1 = shape_line[i], shape_line[i + 1]
                    cavity_clearance = float(x0 + (0.5 - y0) * (x1 - x0) / (y1 - y0))
                else:
                    cavity_clearance = np.nan

            metric_rows.append({
                "job": job["name"],
                "job_id": job["job_id"],
                "role": job["role"],
                "H_number": local_h_number,
                "H_atom_index": h_idx,
                "Pb_atom_index": pb_idx,
                "PbH_A": pb_h_distance,
                "fluidShape_at_H": values_at_h["shape"],
                "electron_density_at_H_e_bohr3": values_at_h["n"],
                "BoundCharge_at_H": values_at_h["nbound"],
                "fluidRhoDiel_at_H": values_at_h["rho_diel"],
                "fluidRhoIon_at_H": values_at_h["rho_ion"],
                "VfluidTot_at_H": values_at_h["vfluid"],
                "cavity_clearance_outward_A": cavity_clearance,
            })
            individual_profiles.append({"t": t, **line})

        average_profile = {"t": individual_profiles[0]["t"]}
        for key in FIELD_FILES:
            average_profile[key] = np.mean(np.stack([profile[key] for profile in individual_profiles], axis=0), axis=0)
        profiles_for_plot[job["name"]] = average_profile

        for i, t_value in enumerate(average_profile["t"]):
            profile_rows.append({
                "job": job["name"],
                "job_id": job["job_id"],
                "distance_outward_from_H_A": float(t_value),
                "fluidShape": float(average_profile["shape"][i]),
                "electron_density_e_bohr3": float(average_profile["n"][i]),
                "BoundCharge": float(average_profile["nbound"][i]),
                "fluidRhoDiel": float(average_profile["rho_diel"][i]),
                "fluidRhoIon": float(average_profile["rho_ion"][i]),
                "VfluidTot": float(average_profile["vfluid"][i]),
            })

    write_csv(OUTDIR / "point_metrics.csv", metric_rows)
    write_csv(OUTDIR / "outward_profiles.csv", profile_rows)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), constrained_layout=True)
    for job in jobs:
        profile = profiles_for_plot[job["name"]]
        axes[0].plot(profile["t"], profile["shape"], label=job["name"])
        axes[1].plot(profile["t"], np.log10(np.clip(profile["n"], 1e-10, None)), label=job["name"])

    axes[0].axhline(0.5, linestyle="--", linewidth=1.0)
    axes[0].set_xlabel("Distance outward from H / Å")
    axes[0].set_ylabel("fluidShape")
    axes[0].set_ylim(-0.05, 1.05)
    axes[0].legend()
    axes[1].set_xlabel("Distance outward from H / Å")
    axes[1].set_ylabel(r"log10 electron density [e / bohr$^3$]")
    axes[1].legend()
    fig.savefig(OUTDIR / "06_outward_profiles.png", dpi=220)
    plt.close(fig)

    print("Proton-well field comparison")
    print("============================")
    print()

    for job in jobs:
        diagnostics = job["fluid_diagnostics"]
        print(job["name"])
        print("-" * len(job["name"]))
        print(f"role:                  {job['role']}")
        print(f"normal FFT grid:       {job['normal_shape']}")
        print(f"fluid field grid:      {job['fields']['shape'].shape}")
        print(f"fluid z sign:          {job['fluid_sign']:+.0f}")
        print(f"fluid z offset:        {job['fluid_offset']:.3f} grid points")
        print(f"<shape> at Pb/O:       {diagnostics['mean_shape_explicit_atoms']:.5f}")
        print(f"max shape at Pb/O:     {diagnostics['max_shape_explicit_atoms']:.5f}")
        print(f"<shape> in vacuum:     {diagnostics['mean_shape_vacuum']:.5f}")

        for row in metric_rows:
            if row["job"] != job["name"]:
                continue
            print(
                f"H{row['H_number']}: Pb-H={row['PbH_A']:.3f} Å  shape(H)={row['fluidShape_at_H']:.4f}  "
                f"n(H)={row['electron_density_at_H_e_bohr3']:.3e}  nbound(H)={row['BoundCharge_at_H']:+.3e}  "
                f"rhoDiel(H)={row['fluidRhoDiel_at_H']:+.3e}  rhoIon(H)={row['fluidRhoIon_at_H']:+.3e}  "
                f"cavity_out={row['cavity_clearance_outward_A']:.3f} Å"
            )
        print()

    print("Interpretation note: VfluidTot is retained as a local diagnostic, but absolute values from separate jobs may carry gauge offsets.")
    print(f"Figures and CSVs written to: {OUTDIR}")


if __name__ == "__main__":
    main()
