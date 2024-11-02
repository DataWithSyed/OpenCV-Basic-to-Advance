# What are contours? they are curve joining all the continuous points along the boundary having the same color or intensity
# It is very helpful in shape analysis, object detection, object recognition
# For better result we use binary images
# Before finding out contours, we find threshold and canny edge detection to find contours on image

import cv2
import numpy as np

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# GETTING NUMBER OF CONTOURS
# HIERARCHY is the optional output vector which is containing the information about image topology
# 1st argument is the image after thresholding
# 2nd argument is the Contour Mode
# 3rd argument is the contour approximation method
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours = " + str(len(contours)))
print(contours[0])      # if we join these coordinates we get the boundary of contour

# DRAW CONTOURS ON THE IMAGE ITSELF
# 1st argument is the image which you want to draw contour on
# 2nd argument are the contours
# 3rd argument is the contour-indexes if -1 give all contour , if 0 give 1st contour, if 2 give 3rd contour
# 4th argument is the color
# 5th argument is the thickness
cv2.drawContours(img, contours, -1, (0,255,255), 3)

cv2.imshow("Image", img)
cv2.imshow('Gray-Image', imgray)


cv2.waitKey(0)
cv2.destroyAllWindows()

