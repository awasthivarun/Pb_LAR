import json
import os

from mpi4py import MPI
import numpy as np
from ase.constraints import FixAtoms
from ase.geometry import find_mic
from ase.io import read, write
from ase.io.trajectory import Trajectory
from ase.mep import DimerControl, MinModeAtoms, MinModeTranslate
from ase.units import Hartree
import pyjdftx


COMMANDS_BASE = """\
van-der-waals D3
elec-cutoff 20 100
electronic-minimize nIterations 100 energyDiffThreshold 1e-07
spintype no-spin
core-overlap-check none
symmetries automatic
fluid LinearPCM
pcm-variant CANDLE
fluid-solvent H2O
fluid-cation Na+ 0.5
fluid-anion F- 0.5
band-projection-params yes no
dump Ionic Ecomponents EigStats Forces
dump Ionic ElecDensity Dtot
dump Ionic BoundCharge VfluidTot FluidDensity
"""

PBC = (True, True, False)


def load_electrochemical_control():
    metadata_path = "metadata.json"
    if not os.path.isfile(metadata_path):
        return COMMANDS_BASE, None

    metadata = json.loads(open(metadata_path).read())
    target_mu = metadata.get("target_mu_Ha")
    charge = metadata.get("charge_e")
    if target_mu is not None and charge is not None:
        raise ValueError("Specify at most one of target_mu_Ha and charge_e in dimer metadata.")

    commands = COMMANDS_BASE
    if target_mu is not None:
        marker = "fluid-anion F- 0.5\n"
        if commands.count(marker) != 1:
            raise RuntimeError("Could not uniquely locate electrolyte block in dimer commands.")
        commands = commands.replace(marker, marker + f"target-mu {float(target_mu):.8f}\n", 1)
    return commands, None if charge is None else float(charge)


def constraint_signature(atoms):
    return [repr(constraint) for constraint in atoms.constraints]


def validate_pair(atoms1, atoms2):
    if len(atoms1) != len(atoms2):
        raise ValueError(f"Dimer endpoint atom counts differ: {len(atoms1)} != {len(atoms2)}")
    if atoms1.get_chemical_symbols() != atoms2.get_chemical_symbols():
        raise ValueError("Dimer endpoint atom species/order differ.")
    if not np.allclose(atoms1.cell.array, atoms2.cell.array, atol=1e-8, rtol=0.0):
        raise ValueError("Dimer endpoint cells differ.")
    if constraint_signature(atoms1) != constraint_signature(atoms2):
        raise ValueError("Dimer endpoint constraints differ.")


def fixed_indices(atoms):
    fixed = set()
    for constraint in atoms.constraints:
        if isinstance(constraint, FixAtoms):
            fixed.update(int(index) for index in constraint.get_indices())
    return sorted(fixed)


def endpoint_displacement(atoms1, atoms2):
    displacement, _ = find_mic(atoms1.positions - atoms2.positions, atoms2.cell, pbc=PBC)
    fixed = fixed_indices(atoms2)
    if fixed:
        displacement[fixed] = 0.0
    if np.linalg.norm(displacement) < 1e-10:
        raise ValueError("Endpoint-derived dimer displacement is effectively zero.")
    return displacement


atoms1 = read("01/CONTCAR", format="vasp")
atoms2 = read("02/CONTCAR", format="vasp")
atoms1.set_pbc(PBC)
atoms2.set_pbc(PBC)
validate_pair(atoms1, atoms2)

dimer_atoms = read("CONTCAR", format="vasp") if os.path.exists("CONTCAR") else atoms2.copy()
dimer_atoms.set_pbc(PBC)
validate_pair(atoms2, dimer_atoms)

if os.path.exists("dimer_vector.npy"):
    displacement_vector = np.load("dimer_vector.npy")
    if displacement_vector.shape != dimer_atoms.positions.shape:
        raise ValueError(
            f"dimer_vector.npy shape {displacement_vector.shape} does not match "
            f"positions {dimer_atoms.positions.shape}."
        )
else:
    displacement_vector = endpoint_displacement(atoms1, atoms2)

commands, charge = load_electrochemical_control()
pyjdftx.initialize(MPI.COMM_WORLD, MPI.COMM_WORLD, "out", False)
dimer_atoms.calc = pyjdftx.ase.JDFTx(
    directory=".", label="job", commands=commands, xc="PBE", kpts=(4, 4, 1, "gamma"), nbands=0,
    smearing=("fermi-dirac", 0.001 * Hartree), write_state=False, charge=charge, center="auto", variable_cell=False,
    pseudopotentials=(
        "/global/cfs/cdirs/m4025/Software/Perlmutter/JDFTx/build-gpu/"
        "pseudopotentials/GBRV_v1.5/$ID_pbe_v1.uspp"
    ),
)

dimer_log = open("dimer.log", "a", buffering=1) if MPI.COMM_WORLD.rank == 0 else None
dimer_control = DimerControl(
    initial_eigenmode_method="displacement", displacement_method="vector", logfile=dimer_log,
    max_num_rot=15, f_rot_max=0.5, f_rot_min=0.05, extrapolate_forces=True, dimer_separation=0.01,
)
dimer_searching_atoms = MinModeAtoms(atoms=dimer_atoms, control=dimer_control)
dimer_searching_atoms.displace(displacement_vector=displacement_vector)


def save_state():
    if MPI.COMM_WORLD.rank == 0:
        write("CONTCAR", dimer_atoms, format="vasp", direct=True)
        np.save("dimer_vector.npy", dimer_searching_atoms.get_eigenmode())


dimer_traj = Trajectory("dimer.traj", "a", dimer_atoms, properties=["energy", "forces"])
opt = MinModeTranslate(dimer_searching_atoms, logfile="dimer_opt.log", trajectory=dimer_traj)
opt.attach(save_state, interval=1)
opt.run(fmax=0.05, steps=400)
dimer_traj.close()
if dimer_log is not None:
    dimer_log.close()
pyjdftx.finalize(True)
