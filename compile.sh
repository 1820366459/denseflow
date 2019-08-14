g++ -o extract_gpu denseFlow_gpu.cpp -I/opt/opencv2.4.13_cuda8.0/include/ -L/opt/opencv2.4.13_cuda8.0/lib -lopencv_video -lopencv_imgproc -lopencv_highgui -lopencv_gpu -lopencv_core -ldl
