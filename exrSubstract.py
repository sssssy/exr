import sys

import exr

a = exr.read(sys.argv[1])
b = exr.read(sys.argv[2])

a[:, :, :3] -= b[:, :, :3]
print(a.shape)

exr.write32(a, sys.argv[3])