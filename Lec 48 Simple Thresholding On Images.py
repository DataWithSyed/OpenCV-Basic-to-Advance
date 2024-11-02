# What is thresholding? It is a very popular segmentation technique used for separating an object from its background
# This process includes comparing each pixel of image with a predefined threshold value
# This process divides pixel of images into 2 types
# 1. 1st group invovles pixel having intensity lower than the threshold value
# 2. 2d group invovles pixel having intensity greater than the threshold value
# Black color have pixel value 0
# White color have pixel value 255

import cv2
import numpy as np

img = cv2.imread('gradient.png', 0)

#1st argument is the source of image
#2nd is the threshold value set by yourself that means it is a Global Value
#3rd argument is the max threshold value of that pic
#4th argument is the threshold type. There are several types which are:
# 1. THRESH_BINARY will assign the pixel 2 values that is in this case 0 & 1
# 2. THRESH_BINARY_INV does just opposite to THRESH_BINARY does
# 3. THRESH_TRUNC when pixel value reached pre-set value gives pixel value 0 otherwise to left or right its value remain same
# 4. THRESH_TOZERO when pixel value is smaller than predefined threshold value it gives 0 that means black color & for greater than threshold value it gives 1
# 5. THRESH_TOZERO_INV does opposite to THRESH_TOZERO

_, th1 =cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
_, th2 =cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 =cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
_, th4 =cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 =cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow('Image', img)
cv2.imshow('Thresholding-Binary', th1)
cv2.imshow('Thresholding-Binary-Inverse', th2)
cv2.imshow('Thresholding-Trunc', th3)
cv2.imshow('Thresholding-ToZero', th4)
cv2.imshow('Thresholding-ToZero-Inverse', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()