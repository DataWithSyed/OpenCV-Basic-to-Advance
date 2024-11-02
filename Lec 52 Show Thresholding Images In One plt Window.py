# I want to show these thresholded images in one window of matplotlib

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', 0)

_, th1 =cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
_, th2 =cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 =cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
_, th4 =cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 =cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original-Image', 'Binary', 'Binary-Inverse', 'Trunc', 'ToZero', 'ToZero-Inverse']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
# 1st argument is the number of rows you want to show on plot
# 2nd argument is the number of columns you want to show on plot
# 3rd argument is the index of image
# plt.imshow(images[i], 'gray') is the showing images one by one
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


#cv2.imshow('Image', img)
#cv2.imshow('Thresholding-Binary', th1)
#cv2.imshow('Thresholding-Binary-Inverse', th2)
#cv2.imshow('Thresholding-Trunc', th3)
#cv2.imshow('Thresholding-ToZero', th4)
#cv2.imshow('Thresholding-ToZero-Inverse', th5)

plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()