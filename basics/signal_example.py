import scipy
from scipy import signal
import numpy as np
import cv2

a = 0.4
kernel = np.array([0.25 - a / 2.0, 0.25, a, 0.25, 0.25 - a / 2.0])
outer = np.outer(kernel, kernel)

# read image
image = cv2.imread('sample_images/anthonylee.jpg', 1)

# open image
# image = cv2.imshow('sample_images/anthonylee.jpg', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image_int = np.uint8(image)
image_float = np.float64(image)

print("============================================================\n")
print(kernel)
print("\n============================================================\n")
print(outer)
print("\n============================================================\n")
print(image_int[0])
print("\n============================================================\n")
print(image_float[0])
