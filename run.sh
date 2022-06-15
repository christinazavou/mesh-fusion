#!/bin/bash
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH --partition=titanx-long    # Partition to submit to
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --time=7-00:00         # Maximum runtime in D-HH:MM
#SBATCH --mem-per-cpu=10000   # Memory in MB per cpu allocated


SOURCE_DIR=${SOURCE_DIR:-"/home/maverkiou/zavou/mesh-fusion"}
PY_EXE=${PY_EXE:-"/home/maverkiou/miniconda2/envs/decorgan/bin/python"}
DATA_PATH=${DATA_PATH:-"/mnt/nfs/work1/kalo/maverkiou/zavou/decorgan-logs/preprocessed_data/groups_june17_uni_nor_components"}

export PYTHONUNBUFFERED="True"
export PYTHONPATH="${PYTHONPATH}:${SOURCE_DIR}"

args="--beta 10.0 --input_size 16 --output_size 128 --train --asymmetry"
args="$args --datapath ${DATA_PATH}"


echo "cd ${SOURCE_DIR} && ${PY_EXE} mymain.py $args"
cd ${SOURCE_DIR} && ${PY_EXE} mymain.py $args 2>&1

