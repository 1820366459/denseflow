__author__ = 'chilu'

import os
import glob
import sys
from pipes import quote
from multiprocessing import Pool, current_process

import argparse
out_path = ''


def run_optical_flow(vid_item, dev_id=0):
    vid_path, vid_name, frame_num = vid_item[0]
    vid_id = vid_item[1]
    ss = vid_path.split('/')
    out_full_path = os.path.join(out_path, vid_name)
    try:
        os.makedirs(out_full_path)
    except OSError:
        pass

    current = current_process()
    dev_id = (int(current._identity[0]) - 1) % NUM_GPU
    flow_x_path = '{}/flow_x'.format(out_full_path)
    flow_y_path = '{}/flow_y'.format(out_full_path)

    cmd = os.path.join(df_path, 'extract_gpu') + ' -f {} -n {} -x {} -y {} -b 20 -t 1 -d {} -s 1'.format(
        quote(vid_path + '/'), quote(frame_num), quote(flow_x_path), quote(flow_y_path), dev_id)

    os.system(cmd)
    print('{} {} done'.format(vid_id, vid_name))
    sys.stdout.flush()
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="extract optical flows")
    parser.add_argument("src_dir")
    parser.add_argument("out_dir")
    parser.add_argument('video_list')
    parser.add_argument("--num_worker", type=int, default=8)
    parser.add_argument("--df_path", type=str, default='./lib/dense_flow/',
                        help='path to the dense_flow toolbox')
    parser.add_argument("--num_gpu", type=int, default=2, help='GPU number')
    parser.add_argument("--div", type=int, default=1)
    parser.add_argument("--divpart", type=int, default=0)

    args = parser.parse_args()

    out_path = args.out_dir
    src_path = args.src_dir
    num_worker = args.num_worker
    df_path = args.df_path
    NUM_GPU = args.num_gpu

    print(args)

    if not os.path.isdir(out_path):
        print("creating folder: " + out_path)
        os.makedirs(out_path)

    vid_list = []
    with open(args.video_list) as f:
        for line in f.readlines():
            ss = line.strip().split(' ')
            vid_list.append((os.path.join(args.src_dir, ss[0]), ss[0], ss[1]))
    total_num = len(vid_list)
    start_no = 0
    end_no = total_num
    if args.div > 1:
        segs = []
        step = int(total_num / args.div)
        for i in range(args.div):
            segs.append(i * step)
        segs.append(total_num)
        start_no = segs[args.divpart]
        end_no = segs[args.divpart + 1]
    vid_list = vid_list[start_no:end_no]
    print('total video:{}\tprocess{}'.format(total_num, len(vid_list)))
    print('start:{}\tend:{}'.format(start_no, end_no))
    pool = Pool(num_worker)
    pool.map(run_optical_flow, zip(vid_list, range(len(vid_list))))
