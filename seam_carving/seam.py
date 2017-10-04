import numpy as np
import cv2

img =  cv2.imread('./images/fig5.png', 0)

sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

print(np.float64(img[0]))
print("==========================")
print(sobel_x[0])

