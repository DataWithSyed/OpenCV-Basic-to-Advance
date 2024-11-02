# Adaptive Thresholding is a method where the threshold value is calculated for the smaller region.
# Threshold is not global for every pixel but is calculated for a smaller region
# So there will be different threshold value for a different regions
# We need this because a image will come with different lighting conditions
# It will give better image result with varying illumination

import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)

#_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 1st argument is the source of image
# 2nd argument is the max value which should be non-zero assigned to the pixel for which the condition is satisfied
# 3rd argument is the ,Adaptive Method and there are 2 types of adaptive methods
# a. ADAPTIVE_THRESH_MEAN_C, the threshold value is the mean of the neighbourhood area
# b. ADAPTIVE_THRESH_GAUSSIAN_C, the threshold value is the weighted sum of neighbourhood gaussian windows and gives better result
# 4th argument is the threshold type
# 5th argument is the block size which means the size of the neighbourhood area
# 6th argument is the constant which is to be subtracted from mean
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Image', img)

#cv2.imshow('Threshold-Binary', th1)
cv2.imshow('Adaptive-Threshold-Mean-C', th2)
cv2.imshow('Adaptive-Threshold-Gaussian-C', th3)


cv2.waitKey(0)
cv2.destroyAllWindows()