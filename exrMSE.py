import os, sys

import numpy as np

import exr

if len(sys.argv) not in [3, 4] or sys.argv[1] == 'help':
    print()
    print('>>> exrMSE.py <<<')
    print('* calculate mse between two given exr images (and save the diff image) *')
    print('* usage: python exrMSE.py img_path1 img_path2 [save_img] *')
    print()
    exit(0)

img1 = exr.read(sys.argv[1])
img2 = exr.read(sys.argv[2])
assert img1.shape == img2.shape

mse = ((img1 - img2) ** 2)
print('mse between {} and {}: {:.1e}'.format(sys.argv[1].split(os.path.sep)[-1], sys.argv[2].split(os.path.sep)[-1], mse.mean()))

if len(sys.argv) == 4:
    exr.write(mse, sys.argv[4])