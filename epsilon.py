import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

### EXAMPLES ###

# Load in gray scale
img = cv2.imread('1_opencv.jpg')

# Show image
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('1_opencv.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Display with Matplotlib
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

# Writes gray scale image load
# cv2.imwrite('1_opencv_gray.jpg', 0)
# cv2.destroyAllWindows()

# Merge gray scale image with color and export, it needs to be same dimension
# img2 = cv2.imread('1_opencv_gray.jpg')
# dst = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
# cv2.imshow('dst', dst)
# cv2.destroyAllWindows()

# Accessing only blue pixel
# blue = img[100, 100, 0]
# print (blue)

# Accessing info
# print (img.shape)
# print (img.size)

##########
## GOAL ##
##########

# Write example

# 1. Change the image apeture +1
    # a. Export to JPG
cv2.imwrite('exports/aperture_plus_1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.imwrite('exports/aperture_plus_1.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    # b. Export to PNG

#2. Change the image apeture +2
    # a. Export to JPG
cv2.imwrite('exports/aperture_plus_2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.imwrite('exports/aperture_plus_2.png', img)
    # b. Export to PNG

#3. Change the image apeture -1
    # a. Export to JPG
cv2.imwrite('exports/aperture_minus_1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.imwrite('exports/aperture_minus_1.png', img)
    # b. Export to PNG

#4. Change the image apeture -2
    # a. Export to JPG
cv2.imwrite('exports/aperture_minus_2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.imwrite('exports/aperture_minus_2.png', img)
    # b. Export to PNG
