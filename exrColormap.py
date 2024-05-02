import sys,pdb

import cv2
import numpy as np
import exr

if len(sys.argv) > 3 or len(sys.argv) < 2:
    print('>>> usage: python exrColormap.py file_name [scale]')
    print('* colormap an EXR image *')
    print('* rescale it into 0~255 by default if $scale is not provided *')
    print('* output: SCALE THRESHOLD (all points with higher value than it will become the pole color) *')
    exit()

img = exr.read(sys.argv[1]).mean(-1)

if len(sys.argv) > 2:
    scale = float(sys.argv[2])
else:
    scale = np.round(255 / img.max(), 2)

new_img = np.clip((img * scale), 0, 255).astype(np.uint8) # scale -> clip -> to BYTE
cv2.imwrite(sys.argv[1].replace('.exr', '_x{}_colormap.png'.format(scale)), 
    cv2.applyColorMap(new_img, cv2.COLORMAP_CIVIDIS))
    # cv2.applyColorMap(new_img, cv2.COLORMAP_VIRIDIS))
print(scale, 255 / scale)
