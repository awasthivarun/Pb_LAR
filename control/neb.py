import os; from mpi4py import MPI
import numpy as np; from ase.io import read
from ase.io.trajectory import Trajectory
from ase.optimize import FIRE
from ase.mep import NEB; from ase.units import Hartree, Bohr
from ase.calculators.singlepoint import SinglePointCalculator
import pyjdftx

def _read_endpoint_energy(s):
    f = next(n for n in os.listdir(s) if n.endswith('Ecomponents'))
    with open(os.path.join(s, f)) as fh: last = [ln.strip() for ln in fh if ln.strip()][-1]
    return float(last.split()[2]) * Hartree

def _read_endpoint_forces(s):
    f = next(n for n in os.listdir(s) if n.endswith('force'))
    return np.loadtxt(os.path.join(s, f), usecols=(2, 3, 4))*(Hartree/Bohr)

def _build_images(nimages):
    image_dirs = [f"{i:02d}" for i in range(0, nimages + 2)]
    initial = read(os.path.join('00', 'CONTCAR'), format='vasp')
    final = read(os.path.join(f"{nimages + 1:02d}", 'CONTCAR'), format='vasp')
    images = [initial]
    for im in image_dirs[1:-1]:
        contcar = os.path.join(im, 'CONTCAR'); poscar = os.path.join(im, 'POSCAR')
        if os.path.exists(contcar): images.append(read(contcar, format='vasp'))
        else: images.append(read(poscar, format='vasp'))
    images.append(final)
    for img in images: img.set_pbc((True, True, False))
    return images, image_dirs

def write_all_contcars():
    for idx, img in enumerate(images[1:-1], 1): img.write(os.path.join(f'{idx:02d}', 'CONTCAR'), format='vasp', direct=True)

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
NIMAGES = 8

comm_world = MPI.COMM_WORLD; comm, i_group = pyjdftx.comm_divide_evenly(comm_world, NIMAGES)
pyjdftx.initialize(comm, comm_world, os.path.join(f'{i_group + 1:02d}', 'out'), False)
images, image_dirs = _build_images(NIMAGES)

for idx, (subdir, image) in enumerate(zip(image_dirs, images)):
    if (idx == 0) or (idx == len(images) - 1):
        E = _read_endpoint_energy(subdir); forces = _read_endpoint_forces(subdir)
        image.calc = SinglePointCalculator(image, energy=E, forces=forces)
    else:
        if i_group + 1 == idx:
            image.calc = pyjdftx.ase.JDFTx(
                directory=subdir, label='job', commands=COMMANDS,
                xc='PBE', kpts=(4, 4, 1, 'gamma'), nbands=0,
                smearing=('fermi-dirac', 0.001*Hartree), write_state=False, 
                charge=None, center='auto', variable_cell=False,
                pseudopotentials='/global/cfs/cdirs/m4025/Software/Perlmutter/JDFTx/build-gpu/pseudopotentials/GBRV_v1.5/$ID_pbe_v1.uspp',
            )
            
neb = NEB(images, parallel=True, climb=False, method='improvedtangent')
neb_traj = Trajectory('neb.traj', 'a', properties=['energy', 'forces'])
opt = FIRE(neb, logfile='neb.log', a=0.1, maxstep=0.2, trajectory=neb_traj)
opt.attach(write_all_contcars, interval=1)
opt.run(fmax=0.05, steps=10)
neb_traj.close(); pyjdftx.finalize(True)

