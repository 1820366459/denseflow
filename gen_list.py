import os
from os import path

root_dir = r'/m/chil/tsn-pytorch/data/kinetics/sample_frame'
list_path = r'sample.lst'
frame_dirs = os.listdir(root_dir)

with open(list_path, 'w') as out:
    for fd in frame_dirs:
        n = len(os.listdir(path.join(root_dir, fd)))
        print(fd, n, 0, file=out)
