import os, sys

import numpy as np

import exr

if len(sys.argv) < 3 or sys.argv[1] == 'help':
    print()
    print('>>> exrAEClamp.py <<<')
    print('* calculate ae between two given exr images while clamped into 0~1 *')
    print('* usage: python exrAEClamp.py img_path1 img_path2 [output_path]*')
    print()
    exit(0)

img1 = np.clip(exr.read(sys.argv[1]), 0, 1)
img2 = np.clip(exr.read(sys.argv[2]), 0, 1)
assert img1.shape == img2.shape

diff = (np.abs(img1 - img2))
print('mse between {} and {}: {}'.format(sys.argv[1].split(os.path.sep)[-1], sys.argv[2].split(os.path.sep)[-1], diff.mean()))
if len(sys.argv) == 4:
    exr.write32(diff, sys.argv[3])
