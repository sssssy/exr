import os, sys

import numpy as np
import matplotlib.pyplot as plt

import exr


if len(sys.argv) < 2:
    print('>>> usage: python exrCurve.py [file_name1 [file_name2...]]')
    print('* draw a curve at the middle position of EXR images *')
    exit()


for i in range(len(sys.argv) - 1):
    img = exr.read(sys.argv[i+1])
    if np.all(img[:, 0] == 0) and np.all(img[0, :] == 0):
        img = img[1:, 1:]

    h, w = img.shape[:2]
    print(h, w)

    mid_h = h // 2

    y = img[mid_h, :, 0]
    x = [i for i in range(w)]

    plt.plot(x, y)
    # plt.ylim( (10e-5, 10e3) )
    plt.yscale('symlog', linthresh=1)
plt.show()