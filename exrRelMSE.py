import sys
import numpy as np
import exr

a = exr.read(sys.argv[1])
b = exr.read(sys.argv[2])
print(a.shape)

maximum = np.where(a > b, a, b)
relmse = (a - b) ** 2 / (maximum + 1e-7)
print(relmse.mean())

if len(sys.argv) > 3:
    exr.write32(relmse, sys.argv[3].replace('.exr', '-{:.4f}.exr'.format(relmse.mean())))