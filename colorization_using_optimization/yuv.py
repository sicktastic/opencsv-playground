# Paper from:
# http://www.cs.huji.ac.il/~yweiss/Colorization/
# Python example from:
# https://github.com/godfatherofpolka/ColorizationUsingOptimizationInPython

import cv2
import math
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import lsqr

# img =  cv2.imread('./images/gray.png')
# img =  cv2.imread('./images/marked.png')
img =  cv2.imread('./images/original.png')
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
