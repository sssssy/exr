import sys
import exr

img1 = exr.read(sys.argv[1])
img2 = exr.read(sys.argv[2])
if len(sys.argv) > 5:
    w1 = float(sys.argv[4])
    w2 = float(sys.argv[5])
else:
    w1 = w2 = 1
exr.write(img1 * w1+img2 * w2, sys.argv[3])