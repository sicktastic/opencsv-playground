import numpy as np
import scipy as sp
import scipy.signal
import cv2

# read image
image = cv2.imread('sample_images/anthonylee.jpg', 1)

# kernels
a = 0.4
kernel = np.array([0.25 - a / 2.0, 0.25, a, 0.25, 0.25 - a / 2.0])
outer = np.outer(kernel, kernel)

# data types
kernel_float = np.float64(outer)
image_float = np.float64(image)

# new_image = np.zeros((image_float.shape[0] * 2, image_float.shape[1] * 2), dtype=np.float64)

# border
# image_border_reflect_101 = cv2.copyMakeBorder(image_float,5,5,5,5,cv2.BORDER_REFLECT_101)

# convolve
# convolve_image = sp.signal.convolve2d(kernel_float, kernel_float)

# scale_image = convolve_image[::2, ::2]

print(kernel)
print("=======")
print(outer)
print("=======")
print(image_float[0:3])

# open image
# image = cv2.imshow('sample_images/anthonylee.jpg', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
