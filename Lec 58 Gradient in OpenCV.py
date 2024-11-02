# Image gradient is a directional change in the intensity or color in an image. It is the building block of image processing
# There are several image gradient methods available. We only discuss 3 of them

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

# Laplacian Methods which uses Laplacian derivatives
# 1st argument is the source of image
# 2nd argument is the data type, using 64 bit float due to negative slope by transforming image from white to black
# 3rd argument is the kernel size
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# We are going to take Absolute value of our laplacian image transformation and convert it into un-signed 8 bit
lap = np.uint8(np.absolute(lap))

# Sobel X and Y Methods are collectively called as Sobel Gradient Representation 0
# Sobel X Method
# 3rd argument is the representation of sobel x method that is dx (order of derivative X)
# 4th argument is the dy (derivative order of Y)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# Just opposite to sobel x method
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
edges = cv2.Canny(img, 100,200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# To combine these both result
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['Image', 'Laplacian', 'Sobel-X Method', 'Sobel-Y Method', 'Canny Edge Detection', 'SobelCombined']
images = [img, lap, sobelX, sobelY, edges, sobelCombined]

for x in range(6):
    plt.subplot(2, 3, x+1),plt.imshow(images[x], 'gray')
    plt.title(titles[x])
    plt.xticks([]), plt.yticks([])

plt.show()