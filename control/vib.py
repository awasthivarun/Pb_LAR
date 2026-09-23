import os; from mpi4py import MPI
from ase.io import read, write
from ase.io.trajectory import Trajectory
from ase.vibrations import Vibrations
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

def read_atoms():
    fname = 'CONTCAR' if os.path.exists('CONTCAR') else 'POSCAR'
    atoms = read(fname)
    return atoms

pyjdftx.initialize(MPI.COMM_WORLD, MPI.COMM_WORLD, 'out', False)  
calc = pyjdftx.ase.JDFTx(
    directory='.', label='job', commands = COMMANDS,
    xc='PBE', kpts=(4, 4, 1, 'gamma'), nbands=0,
    smearing=('fermi-dirac', 0.001*Hartree), write_state=False,  
    charge=None, center='auto', variable_cell=False,
    pseudopotentials='/global/cfs/cdirs/m4025/Software/Perlmutter/JDFTx/build-gpu/pseudopotentials/GBRV_v1.5/$ID_pbe_v1.uspp', 
)

atoms = read_atoms(); atoms.set_pbc((True, True, False))
atoms.calc = calc

vib = Vibrations(atoms, name='vib', delta=0.01)
vib.run()
vib.summary(log='vib.log')
pyjdftx.finalize(True)
