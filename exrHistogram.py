import sys,pdb

from matplotlib import pyplot as plt
import numpy as np
import exr

if len(sys.argv) not in [2, 3, 5]:
    print('>>> usage: python exrHistogram.py file_name [num_bins] [min] [max]')
    print('* generate the histogram for an EXR image (grayscale) of $num_bins *')
    exit()

img = exr.read(sys.argv[1]).mean(-1)

if len(sys.argv) >= 3:
    num_bins = int(sys.argv[2])
else:
    num_bins = 10

if len(sys.argv) == 5:
    minimum = float(sys.argv[3])
    maximum = float(sys.argv[4])
else:
    maximum, minimum = img.max(), img.min()
print(minimum, maximum)

np.set_printoptions(suppress=True, threshold=np.inf, linewidth=120)

pos_bins = np.logspace(np.log(1e-4), np.log(maximum), num=num_bins, endpoint=True, base=np.exp(1))
neg_bins = -np.logspace(np.log(1e-4), np.log(-minimum), num=num_bins, endpoint=True, base=np.exp(1))
bins = np.concatenate([neg_bins[::-1], pos_bins])

hist, bin_edges = np.histogram(img, bins=bins, density=True)
norm = hist[np.argsort(hist)[-num_bins//10]]
print(norm)
hist[hist > norm] = hist[hist > norm] / norm + norm
plt.plot(bins[:-1], hist)
# plt.bar(bins[:-1], hist, width=0.001)
plt.title('Histogram of '+sys.argv[1])
plt.yscale('log')
plt.show()