# Morphological Transformation like erosion, dilation, opening and closing
# Morphological Transformation are some simple operations based on the image shape
# These are performed on Binary Images
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

kernal = np.ones((3,3), np.uint8)
dilation  = cv2.dilate(mask, kernal, iterations=3)


titles = ['Image', 'Mask', 'Dilation']
images = [img, mask, dilation]

for i in range(3):
    plt.subplot(1, 3, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()