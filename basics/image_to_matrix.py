import numpy as np
import cv2

IMAGE = cv2.imread('sample_images/anthonylee.jpg', 1)

# Show image
# cv2.imshow('sample_images/anthonylee.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image_to_matrix = np.float64(IMAGE)
# print(image_to_matrix)
# print(image_to_matrix[range(1, 10)])
print("There are", len(image_to_matrix), "matrices here.")
