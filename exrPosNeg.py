import sys

import numpy as np

import exr

if len(sys.argv) != 2 or sys.argv[1] == 'help':
    print()
    print('>>> exrPosNeg.py <<<')
    print('* mark positive points in red and negative points in green *')
    print('* usage: python exrPosNeg.py img_path *')
    print()
    exit(0)

def pos_neg(a):
    '''
        a should be a gray scale exr image of shape [h, w] or [h, w, 1]
        or we will calculate the mean value along the last dimension.
    '''
    if len(a.shape) > 2 and a.shape[2] != 1:
        a = a.mean(-1)
    a = a.reshape(a.shape[0], a.shape[1])
    b = np.zeros([a.shape[0], a.shape[1], 3], dtype=np.float32)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i, j] >= 0:
                b[i, j, 1] = a[i, j]
            else:
                b[i, j, 0] = -a[i, j]
    return b

if __name__ == '__main__':
    pos_neg(sys.argv[1])