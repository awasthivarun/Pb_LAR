import os; from mpi4py import MPI
import numpy as np; from ase.io import read, write
from ase.io.trajectory import Trajectory
from ase.mep import DimerControl, MinModeAtoms, MinModeTranslate
from ase.units import Hartree
import pyjdftx

COMMANDS = """\
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

atoms1 = read('01/CONTCAR', format='vasp'); atoms2 = read('02/CONTCAR', format='vasp')
common_pbc = [True, True, False]
atoms1.set_pbc(common_pbc); atoms2.set_pbc(common_pbc)
dimer_atoms = atoms2.copy()

if os.path.exists('CONTCAR'):
    dimer_atoms = read('CONTCAR', format='vasp')
    dimer_atoms.set_pbc(common_pbc)
if os.path.exists('dimer_vector.npy'):
    displacement_vector = np.load('dimer_vector.npy')
else:
    cell = dimer_atoms.get_cell()
    diff = atoms1.get_positions() - atoms2.get_positions()
    diff = diff - np.round(diff @ np.linalg.inv(cell)) @ cell
    displacement_vector = np.zeros_like(diff)
    displacement_vector[26] = diff[26]

pyjdftx.initialize(MPI.COMM_WORLD, MPI.COMM_WORLD, 'out', False)
dimer_atoms.calc = pyjdftx.ase.JDFTx(
    directory='.', label='job', commands = COMMANDS,
    xc='PBE', kpts=(4, 4, 1, 'gamma'), nbands=0,
    smearing=('fermi-dirac', 0.001*Hartree), write_state=False,  
    charge=-1, center='auto', variable_cell=False,
    pseudopotentials='/global/cfs/cdirs/m4025/Software/Perlmutter/JDFTx/build-gpu/pseudopotentials/GBRV_v1.5/$ID_pbe_v1.uspp', 
)

dimer_log_file = open('dimer.log', 'a', buffering=1) if MPI.COMM_WORLD.rank == 0 else None
dimer_control = DimerControl(initial_eigenmode_method='displacement', 
                             displacement_method='vector', logfile=dimer_log_file,
                             max_num_rot=15, f_rot_max=0.5, f_rot_min=0.05,
                             extrapolate_forces=True, dimer_separation=0.01)
dimer_searching_atoms = MinModeAtoms(atoms=dimer_atoms, control=dimer_control)
dimer_searching_atoms.displace(displacement_vector=displacement_vector)

def save_state():
    write('CONTCAR', dimer_atoms, format='vasp', direct=True)
    if MPI.COMM_WORLD.rank == 0: np.save('dimer_vector.npy', dimer_searching_atoms.get_eigenmode())

dimer_traj = Trajectory('dimer.traj', 'a', dimer_atoms, properties=['energy', 'forces'])
opt = MinModeTranslate(dimer_searching_atoms, logfile='dimer_opt.log', trajectory=dimer_traj)
opt.attach(save_state, interval=1)
opt.run(fmax=0.05, steps=400)
dimer_traj.close(); pyjdftx.finalize(True)