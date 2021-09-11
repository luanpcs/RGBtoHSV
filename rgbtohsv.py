import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("colors.png")
img_rgb = np.array(img)
l, c, p = img_rgb.shape

img_hsv = np.zeros(shape=img_rgb.shape, dtype=np.float64)
img_hsv_verify = np.array(img.convert('HSV'))[:, :, :3]
for i in range(l):
    for j in range(c):
        r = img_rgb[i, j, 0]/255
        g = img_rgb[i, j, 1]/255
        b = img_rgb[i, j, 2]/255
        cmax = max(r,g,b)
        cmin = min(r,g,b)
        d = cmax - cmin
        if (d == 0):
          h = 0
        elif (cmax == r and g>=b):
          h = 60*((g-b)/d)
        elif (cmax == r and g<b):
          h = 60*((g-b)/d)+360
        elif (cmax == g):
          h = 60*((b-r)/d)+120
        elif (cmax == b):
          h = 60*((r-g)/d)+240

        if (cmax == 0):
          s = 100
        else:
          s = (d/cmax)
        h = h/360
        v = cmax

        img_hsv[i, j, 0] = h
        img_hsv[i, j, 1] = s
        img_hsv[i, j, 2] = v

plt.figure(figsize=(8, 8))
plt.subplot(3, 1, 1)
plt.imshow(img_rgb)

plt.subplot(3, 1, 2)
plt.imshow(img_hsv)

plt.subplot(3, 1, 3)
plt.imshow(img_hsv_verify)