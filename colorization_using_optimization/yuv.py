# Paper from:
# http://www.cs.huji.ac.il/~yweiss/Colorization/

import cv2
import matplotlib.pyplot as plt
import numpy as np

img =  cv2.imread('./images/anthonylee.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

print(img[0])
print(img[0][0])
print(img[0][1])
print(img[0][2])
print("--------------------")
print(img_yuv[0])
print(img_yuv[0][0])
print(img_yuv[0][1])
print(img_yuv[0][2])
print("--------------------")

# YUV Color Space
# Y is the monochromatic luminance channel
# which will refer to simply as intensity,
# while U and V are the chrominance channels,
# encoding the color.

# calculate weights of neighbors

# w_rs = e^{-(Y(s)-Y(r))^2 / 2\sigma_r^2}

# where r is the index of the center, s the index of a neighbour and

# sigma_r is the variance in a neighbourhood around r.
