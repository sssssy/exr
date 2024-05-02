import sys

import numpy as np

import exr

file_name_R, file_name_G, file_name_B = sys.argv[1], sys.argv[2], sys.argv[3]
R = exr.read(file_name_R)[..., 0:1]
G = exr.read(file_name_G)[..., 0:1]
B = exr.read(file_name_B)[..., 0:1]

exr.write(np.concatenate([R, G, B], axis=-1), sys.argv[4])