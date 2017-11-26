import math
import matplotlib.pyplot as plt
import numpy as np
import cv2

# import images
bw =  cv2.imread('./images/bw.bmp')
marked =  cv2.imread('./images/marked.bmp')
example = cv2.imread('./images/example.png')

yuv = cv2.cvtColor(example, cv2.COLOR_BRG2YUV)

print(yuv)
