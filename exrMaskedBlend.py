import sys
import numpy as np
import exr

img1 = exr.read(sys.argv[1])
img2 = exr.read(sys.argv[2])
mask = exr.read(sys.argv[3])
exr.write(np.where(mask, img1, img2), sys.argv[4])