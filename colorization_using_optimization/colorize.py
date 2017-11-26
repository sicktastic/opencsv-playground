import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import lsqr

# import images
bw =  cv2.imread('./images/bw.bmp')
marked =  cv2.imread('./images/marked.bmp')

yuv = cv2.cvtColor(marked, cv2.COLOR_BGR2YUV)

y = yuv[:,:,0]
u = yuv[:,:,1]
v = yuv[:,:,2]

print(y[0,1], u[0,1], v[0,1])
