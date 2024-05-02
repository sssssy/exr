import sys

import numpy as np

import exr

def normalize(img):
    norm = np.sqrt(img[:, :, 0] ** 2 + img[:, :, 1] ** 2 + img[:, :, 2] ** 2)
    return img / norm.reshape(*norm.shape, 1)

if len(sys.argv) not in [3, 4]:
    print()
    print('>>> scaleNormalmap.py <<<')
    print('* scale a normalmap (0~1) while keeping the ratio between xy (i.e., scale along z) *')
    print('* usage: python scaleNormalmap.py img_path scale [out_path] *')
    print()
    exit(0)


file_name = sys.argv[1]
scale = float(sys.argv[2])
out_path = sys.argv[3] if len(sys.argv) == 4 else file_name.replace('.exr', f'_scale{scale}.exr')

img = exr.read(file_name)
print(img.shape)

x = (img[:, :, 0] - 0.5) * 2
y = (img[:, :, 1] - 0.5) * 2
z = (img[:, :, 2] - 0.5) * 2

xz = x / z * scale
yz = y / z * scale

x1 = xz * z
y1 = yz * z

img1 = np.stack([x1, y1, z], axis=2)
img1 = normalize(img1)

img1 = (img1 + 1) / 2

exr.write(img1, out_path)