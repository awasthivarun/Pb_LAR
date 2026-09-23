#!/usr/bin/env python

from pathlib import Path
import argparse

import numpy as np
from ase.io import read, write
from ase.mep import NEB


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create MIC-aware IDPP-interpolated images for an ASE NEB calculation."
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path("."),
        help="NEB calculation directory containing 00/, 01/, ..., final endpoint directory.",
    )
    parser.add_argument(
        "--nimages",
        type=int,
        default=8,
        help="Number of intermediate NEB images. Default: 8.",
    )
    parser.add_argument(
        "--initial",
        type=str,
        default="00/CONTCAR",
        help="Initial endpoint relative to --dir. Default: 00/CONTCAR.",
    )
    parser.add_argument(
        "--final",
        type=str,
        default=None,
        help="Final endpoint relative to --dir. Default: <nimages+1>/CONTCAR.",
    )
    parser.add_argument(
        "--overwrite-poscar",
        action="store_true",
        help="Allow replacement of existing intermediate POSCAR files.",
    )
    return parser.parse_args()


def constraint_signature(atoms):
    signature = []

    for constraint in atoms.constraints:
        signature.append(repr(constraint))

    return signature


def validate_endpoints(initial, final):
    if len(initial) != len(final):
        raise ValueError(
            f"Endpoint atom counts differ: initial={len(initial)}, final={len(final)}"
        )

    initial_symbols = initial.get_chemical_symbols()
    final_symbols = final.get_chemical_symbols()

    if initial_symbols != final_symbols:
        mismatch = [
            (i, a, b)
            for i, (a, b) in enumerate(zip(initial_symbols, final_symbols))
            if a != b
        ]

        raise ValueError(
            "Endpoint atom species/order differ. "
            f"First mismatches: {mismatch[:10]}"
        )

    if not np.allclose(initial.cell.array, final.cell.array, atol=1e-8, rtol=0.0):
        raise ValueError("Endpoint cells differ.")

    if tuple(initial.pbc) != tuple(final.pbc):
        raise ValueError(
            f"Endpoint PBC differ: initial={initial.pbc}, final={final.pbc}"
        )

    if constraint_signature(initial) != constraint_signature(final):
        raise ValueError(
            "Endpoint constraints differ. Check selective dynamics / fixed atoms."
        )


def maximum_neighbor_displacement(images):
    values = []

    for left, right in zip(images[:-1], images[1:]):
        displacement = right.positions - left.positions
        displacement, _ = ase_find_mic(displacement, left.cell, left.pbc)
        distances = np.linalg.norm(displacement, axis=1)
        values.append(float(np.max(distances)))

    return values


def ase_find_mic(displacement, cell, pbc):
    from ase.geometry import find_mic

    return find_mic(displacement, cell, pbc=pbc)


def main():
    args = parse_args()

    if args.nimages < 1:
        raise ValueError("--nimages must be at least 1.")

    neb_dir = args.dir.expanduser().resolve()

    if not neb_dir.is_dir():
        raise FileNotFoundError(f"NEB directory does not exist: {neb_dir}")

    final_relpath = args.final
    if final_relpath is None:
        final_relpath = f"{args.nimages + 1:02d}/CONTCAR"

    initial_path = neb_dir / args.initial
    final_path = neb_dir / final_relpath

    if not initial_path.is_file():
        raise FileNotFoundError(f"Initial endpoint not found: {initial_path}")

    if not final_path.is_file():
        raise FileNotFoundError(f"Final endpoint not found: {final_path}")

    initial = read(initial_path, format="vasp")
    final = read(final_path, format="vasp")

    initial.set_pbc((True, True, False))
    final.set_pbc((True, True, False))

    validate_endpoints(initial, final)

    intermediate_dirs = [
        neb_dir / f"{i:02d}"
        for i in range(1, args.nimages + 1)
    ]

    for directory in intermediate_dirs:
        contcar = directory / "CONTCAR"
        poscar = directory / "POSCAR"

        if contcar.exists():
            raise FileExistsError(
                f"Refusing to regenerate images because a restart CONTCAR exists: {contcar}"
            )

        if poscar.exists() and not args.overwrite_poscar:
            raise FileExistsError(
                f"Intermediate POSCAR already exists: {poscar}\n"
                "Use --overwrite-poscar only if this NEB has not started."
            )

    images = [initial.copy() for _ in range(args.nimages + 1)]
    images.append(final.copy())

    neb = NEB(images)
    neb.interpolate(method="idpp", mic=True)

    for i, image in enumerate(images[1:-1], start=1):
        directory = neb_dir / f"{i:02d}"
        directory.mkdir(parents=True, exist_ok=True)

        write(
            directory / "POSCAR",
            image,
            format="vasp",
            direct=True,
            vasp5=True,
        )

    neighbor_displacements = maximum_neighbor_displacement(images)

    print(f"NEB directory:       {neb_dir}")
    print(f"Initial endpoint:    {initial_path}")
    print(f"Final endpoint:      {final_path}")
    print(f"Intermediate images: {args.nimages}")
    print("Interpolation:       IDPP, MIC=True")
    print()
    print("Maximum atomic displacement between neighboring images")
    print("-------------------------------------------------------")

    for i, value in enumerate(neighbor_displacements):
        print(f"{i:02d} -> {i + 1:02d}: {value:8.4f} A")

    print()
    print(
        f"Largest neighboring-image displacement: "
        f"{max(neighbor_displacements):.4f} A"
    )
    print("Intermediate POSCAR files written successfully.")


if __name__ == "__main__":
    main()