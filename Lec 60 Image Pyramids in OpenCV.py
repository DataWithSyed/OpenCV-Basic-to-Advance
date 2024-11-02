# We are using images with constant size, sometimes we need to work with images having different resolutions
# Let suppose i want to detect faces from images. Every face is different from other
# Image Pyramids are used to create images of different resolution and then we search for an objects like face in these images
# There are 2 types of image pyramids which are:
# 1. Gaussian Pyramid  >  it is repeat filtering and sub-sampling of an image. It contains 2 function pyr-down and pyr-up
# 2. Laplacian Pyramid  >  formed from gaussian pyramids
# Pyramids are used to blend and re-construct the images

import cv2
import numpy as np
img = cv2.imread('lena.jpg')

# GAUSSIAN PYRAMID
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer )
   # cv2.imshow(str(i), layer)

#lr = cv2.pyrDown(img)
#lr1 = cv2.pyrDown(lr)

# When you use pyr-up, it will blur that is losing its information
#hr = cv2.pyrUp(img)

# LAPLACIAN PYRAMID
# take top level layer of gaussian pyramid
layer = gp[5]
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Upper Level Gaussian Pyramid', layer)
cv2.imshow('Image', img)
#cv2.imshow('Pyr-Down', lr)
#cv2.imshow('Pyr-Down-Again', lr1)
#cv2.imshow('Pyr-Up', hr)

cv2.waitKey(0)
cv2.destroyAllWindows()