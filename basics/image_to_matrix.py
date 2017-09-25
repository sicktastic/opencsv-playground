import numpy as np
import scipy as sp
import scipy.signal
import cv2

# def generating_kernel(a):
#   w_1d = np.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
#   return np.outer(w_1d, w_1d)


# outimage = scipy.signal.convolve2d(kernel,kernel,'same')

# ------------------------------------------------------------------
#
#
#
#                                          000000
#             Upsample   A0B0     Pad      0A0B0B   Convolve   zyxw
#        AB   ------->   0000   ------->   000000   ------->   vuts
#        CD              C0D0    BORDER    0C0D0D     keep     rqpo
#        EF              0000   REFLECT    000000    valid     nmlk
#                        E0F0              0E0F0F              jihg
#                        0000              000000              fedc
#                                          0E0F00

arr = np.array([[1, 2, 1, 10, 20], [3, 4, 3, 30, 40], [5, 6, 5, 50, 60], [7, 8, 7, 70, 80], [9, 10, 9, 90, 100]])


arr_shape = arr.shape
x = arr_shape[0]
y = arr_shape[1]
expand_arr_with_zeros = np.zeros([x * 2, y * 2])

expand_arr_with_zeros[::2, ::2] = arr[:, :]

a_array = []
a_array.append(arr)
print(a_array)

b_array = [arr]
print(b_array)

for i in range (0, 10):
    print("Hello")

# print(arr)
# print("---------------")
# print(expand_arr_with_zeros)


# ------------------------------------------------------------------

# image = cv2.imread('sample_images/anthonylee.jpg', 1)
# image = np.float64(image)
# image = image[5:-5, 5:-5]
# kernel = generating_kernel(0.4)
# kernel = np.float64(kernel)

# outimage = scipy.signal.convolve2d(image,kernel,'same')

# print(kernel)
# print("------------------")
# print(image)
