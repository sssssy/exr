from sys import argv

import numpy as np
import exr

if len(argv) > 3 or len(argv) < 2:
    exit('>>> Usage: python exrTranspose.py file_name [output_name]')

file_name = argv[1]
output_name = argv[2] if len(argv) > 2 else file_name.replace('.exr', '_t.exr')
exr.write32(np.transpose(exr.read(file_name), (1, 0, 2)), output_name)