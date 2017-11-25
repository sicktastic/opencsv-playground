# Paper from:
# http://www.cs.huji.ac.il/~yweiss/Colorization/
# Python example from:
# https://github.com/godfatherofpolka/ColorizationUsingOptimizationInPython

import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import lsqr

img =  cv2.imread('./images/gray.png')
# img =  cv2.imread('./images/marked.png')
# img =  cv2.imread('./images/original.png')
b,g,r = cv2.split(img)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_rgb = cv2.merge([r,g,b])
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("1. BRG  --------------------")
print(img[0, :5])
print("2. YUV --------------------")
print(img_yuv[0, :5])
print("3. RGB --------------------")
print(img_rgb[0, :5])
print("4. Gray -------------------")
print(img_rgb[0, :5])
print("5. Shape -------------------")
print("Image BRG Shape:", img.shape)
print("Image YUV Shape:", img_yuv.shape)
print("Image RGB Shape:", img_rgb.shape)
print("Image Gray Shape:", img_rgb.shape)

# Helper functions to convert from RGB color space to YIQ color space and vice-versa.

# Values for conversion matrices taken from http://en.wikipedia.org/wiki/YIQ#Formulas

# YUV Color Space
# Y is the monochromatic luminance channel
# which will refer to simply as intensity,
# while U and V are the chrominance channels,
# encoding the color.

# calculate weights of neighbors

# w_rs = e^{-(Y(s)-Y(r))^2 / 2\sigma_r^2}

# where r is the index of the center, s the index of a neighbour and

# sigma_r is the variance in a neighbourhood around r.
