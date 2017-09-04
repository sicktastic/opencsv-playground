import numpy
import cv2

# load in gray scale
img = cv2.imread('1_opencv.jpg', 0)
cv2.imshow('1_opencv.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
