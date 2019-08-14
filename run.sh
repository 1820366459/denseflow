export LD_LIBRARY_PATH=/opt/opencv2.4.13_cuda8.0/lib

./extract_gpu -f /ssd/kinetics/frame400_new/val/e1Lxov1lYH8_000276_000286/ -n 300 -x test/flow_x -y test/flow_y -b 20 -t 1 -d 0 -s 1
