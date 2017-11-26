import math
import matplotlib.pyplot as plt
import numpy as np
import cv2

# colorization images
gray =  cv2.imread('./images/gray.bmp')
marked =  cv2.imread('./images/marked.bmp')

# from matlab code colorize.m
solver = 2

gray = gray.astype(np.float32) / 255
marked = marked.astype(np.float32) / 255

# yuv = cv2.cvtColor(marked, cv2.COLOR_BGR2YUV)

# y, u, v = yuv[:,:,0], yuv[:,:,1], yuv[:,:,2]

# from matlab code colorize.m
# max_d = np.floor(np.log(min(yuv.shape[0],yuv.shape[1]))/np.log(2)-2)

# moved this to private repo on 11/26/2017 11:23:00
