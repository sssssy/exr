import sys

import exr

file_name = sys.argv[1]
img = exr.read(file_name)

exr.writeMono32(img[:, :, 0], file_name.replace('.exr', '_R.exr'))
exr.writeMono32(img[:, :, 1], file_name.replace('.exr', '_G.exr'))
exr.writeMono32(img[:, :, 2], file_name.replace('.exr', '_B.exr'))