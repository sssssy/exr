import os, sys
from glob import glob
from pdb import set_trace as debug

import numpy as np
import matplotlib.pyplot as plt

import exr

def log(a):
    return np.log(a)

def log1(a):
    return np.log1p(a)

def log03(a):
    return np.log(a + 0.3)

def log001(a):
    return np.log(a + 0.01)

x = np.arange(0, 0.1, 0.0001)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, log(x), label='log(x)')
plt.plot(x, log1(x), label='log1(x)')
plt.plot(x, log03(x), label='log0.3(x)')
plt.plot(x, log001(x), label='log0.01(x)')
plt.legend()
plt.axhline(0, color='red')
plt.axvline(0, color='red')
plt.show()