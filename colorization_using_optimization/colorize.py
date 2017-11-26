import math
import matplotlib.pyplot as plt
import numpy as np
import cv2

# import images
bw =  cv2.imread('./images/bw.bmp')
marked =  cv2.imread('./images/marked.bmp')
example = cv2.imread('./images/example.png')

yuv = cv2.cvtColor(marked, cv2.COLOR_BGR2YUV)

y = yuv[:,:,0]
u = yuv[:,:,1]
v = yuv[:,:,2]

# print(y[0,1], u[0,1], v[0,1])

# from matlab code colorize.m line 23
max_d = np.floor(np.log(min(yuv.shape[0],yuv.shape[1]))/np.log(2)-2)
