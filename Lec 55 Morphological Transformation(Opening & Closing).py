# When we perform Morphological Transformation, there are 2 thing required which are
# 1. Original image
# 2. A Structuring Element or Kernal(tells you how to change the value of any given pixel by combining it with different amounts of the neighbouring pixels) which decides the nature of images

import cv2
import numpy as np
from matplotlib import pyplot as plt

# As you Know morphological transformation mostly deals with binary images so we mask it using thresholding
img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# For removing these black dot from circle we use DILATION
# For Complete Removing of black dot we use Iterations

# 1st argument is the source of images
# 2nd argument is the kernel which is square or any shape which we apply on the image

kernal = np.ones((5,5), np.uint8)

# Erosion will work just like soil erosion
erosion = cv2.erode(mask, kernal, iterations=1)
dilation  = cv2.dilate(mask, kernal, iterations=3)

# Opening is another name of Erosion followed by Dilation
# 1st argument is the source, 2nd is the type of morphological transformaion, 3rd is kernal
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Opening is another name of Dilation followed by Erosion
# 1st argument is the source, 2nd is the type of morphological transformaion, 3rd is kernal
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()