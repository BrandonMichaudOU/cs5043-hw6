#!/bin/bash
#
#SBATCH --partition=debug
#SBATCH --cpus-per-task=16
#SBATCH --mem=1G
#SBATCH --output=outputs/hw6_%j_stdout.txt
#SBATCH --error=outputs/hw6_%j_stderr.txt
#SBATCH --time=00:05:00
#SBATCH --job-name=hw6
#SBATCH --mail-user=brandondmichaud@ou.edu
#SBATCH --mail-type=ALL
#SBATCH --chdir=/home/cs504319/cs5043-hw6
#SBATCH --array=0

. /home/fagg/tf_setup.sh
conda activate tf
module load cuDNN/8.9.2.26-CUDA-12.2.0


python hw5_base.py -vv @exp.txt @rnn.txt --exp_index $SLURM_ARRAY_TASK_ID --cpus_per_task $SLURM_CPUS_PER_TASK --dataset /home/fagg/datasets/pfam