import numpy as np
import cv2
from matplotlib import pyplot as plt

# load in gray scale
img = cv2.imread('1_opencv.jpg', 0)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('1_opencv.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
