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

yuv = cv2.cvtColor(bw, cv2.COLOR_BRG2YUV)

print(yuv[0])
