# When we perform Morphological Transformation, there are 2 thing required which are
# 1. Original image
# 2. A Structuring Element or Kernal(tells you how to change the value of any given pixel by combining it with different amounts of the neighbouring pixels) which decides the nature of images

import cv2
import numpy as np
from matplotlib import pyplot as plt

# As you Know morphological transformation mostly deals with binary images so we mask it using thresholding
img = cv2.imread('j.jpg', 0)
_, mask = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)

# For removing these black dot from circle we use DILATION
# For Complete Removing of black dot we use Iterations

# 1st argument is the source of images
# 2nd argument is the kernel which is square or any shape which we apply on the image

kernal = np.ones((5,5), np.uint8)

# Opening is another name of Erosion followed by Dilation
# 1st argument is the source, 2nd is the type of morphological transformaion, 3rd is kernal
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Opening is another name of Dilation followed by Erosion
# 1st argument is the source, 2nd is the type of morphological transformaion, 3rd is kernal
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal)
cross = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernal)

titles = ['Image', 'Mask', 'Opening', 'Closing', 'Gradient', 'Top-Hat', 'Black-Hat', 'Cross']
images = [img, mask, opening, closing, gradient, top_hat, black_hat, cross]

for i in range(8):
    plt.subplot(2, 4, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()