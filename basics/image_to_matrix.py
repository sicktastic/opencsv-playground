import numpy as np
import scipy as sp
import scipy.signal
import cv2

def generating_kernel(a):
  w_1d = np.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
  return np.outer(w_1d, w_1d)

image = cv2.imread('sample_images/anthonylee.jpg', 1)
image = np.float64(image)
image = image[5:-5, 5:-5]
kernel = generating_kernel(0.4)
kernel = np.float64(kernel)

outimage = scipy.signal.convolve2d(kernel,kernel,'same')

print(kernel)
print("------------------")
print(image)
