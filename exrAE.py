#!python
import os, sys

import numpy as np

import exr

if len(sys.argv) not in [3, 4] or sys.argv[1] == 'help':
    print()
    print('>>> exrAE.py <<<')
    print('* calculate abs error between two given exr images*')
    print('* usage: python exrAE.py img_path1 img_path2 [out_path] *')
    print()
    exit(0)

img1 = exr.read(sys.argv[1])
img2 = exr.read(sys.argv[2])
assert img1.shape == img2.shape

ae = np.abs(img1 - img2).mean()
print('AE between {} and {}: {}'.format(sys.argv[1].split(os.path.sep)[-1], sys.argv[2].split(os.path.sep)[-1], ae))

if len(sys.argv) > 3:
    out_path = sys.argv[3]
    exr.write32(np.abs(img1 - img2), out_path.replace('.exr', '-{:.4f}.exr'.format(ae)))