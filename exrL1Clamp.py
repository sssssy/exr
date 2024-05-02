import os, sys

import numpy as np

import exr

if len(sys.argv) != 3 or sys.argv[1] == 'help':
    print()
    print('>>> exrL1Clamp.py <<<')
    print('* calculate L1 between two given exr images while clamped into 0~1 *')
    print('* usage: python exrL1Clamp.py img_path1 img_path2 *')
    print()
    exit(0)

img1 = exr.read(sys.argv[1])
img2 = exr.read(sys.argv[2])
assert img1.shape == img2.shape

mse = ((img1 - img2) ** 2).mean()
print('mse between {} and {}: {}'.format(sys.argv[1].split(os.path.sep)[-1], sys.argv[2].split(os.path.sep)[-1], mse))
