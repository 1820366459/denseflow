#!/usr/bin/env bash

export LD_LIBRARY_PATH=/opt/opencv2.4.13_cuda8.0/lib

SRC_FOLDER=/m/chil/tsn-pytorch/data/kinetics/sample_frame/
OUT_FOLDER=sample_of/
VIDEO_LIST=/m/chil/denseflow/sample.lst
NUM_WORKER=3

echo "Extracting optical flow from videos in folder: ${SRC_FOLDER}"
date
python -u build_of_gpu.py ${SRC_FOLDER} ${OUT_FOLDER} ${VIDEO_LIST} --df_path=./ --num_worker=${NUM_WORKER} --num_gpu 1
date
