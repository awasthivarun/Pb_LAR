#!/bin/bash
#SBATCH -A m4283_g
#SBATCH -C gpu
#SBATCH -q shared
#SBATCH --time 04:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -c 32
#SBATCH --gpus-per-task=1
#SBATCH -o go.%j
#SBATCH --job-name=go_jobname

source /opt/cray/pe/cpe/26.03/restore_lmod_system_defaults.sh
module use /global/cfs/cdirs/m4025/Software/Perlmutter/modules
module load pyjdftx
export SLURM_CPU_BIND="cores"
export JDFTX_CACHE_SIZE=36000
export MPICH_GPU_SUPPORT_ENABLED=1

srun python go.py
