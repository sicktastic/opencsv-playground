# Paper from:
# http://www.cs.huji.ac.il/~yweiss/Colorization/

import cv2
import matplotlib.pyplot as plt
import numpy as np

img =  cv2.imread('./images/anthonylee.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

print(img[0])
print("--------------------")
print(img_yuv[0])
print("--------------------")

