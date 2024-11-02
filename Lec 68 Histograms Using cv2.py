import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', 0)

# 1st argument is the source or image but in the SQUARE BRACKETS
# 2nd argument is the channel we use grayscale so use 0
# 3rd argument is the image mask. For histogram of full image we give None
# 4th argument is the hist size which is representation of bin-counts
# 5th argument is the range
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()