import sys

import exr

file_name = sys.argv[1]
img = exr.read(file_name)

exr.write(img.mean(-1), file_name.replace('.exr', '_grey.exr'))