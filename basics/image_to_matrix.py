import numpy as np
import cv2

IMAGE = cv2.imread('./sample_images/anthonylee.jpg', 1)

image_to_matrix = np.float64(IMAGE)

print(image_to_matrix)
print("There are", len(image_to_matrix), "matrices here.")
