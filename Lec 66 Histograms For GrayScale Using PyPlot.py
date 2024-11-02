# What are Histograms? A graph or a plot which gives you an overall idea about intensity distribution of an image
# Lets say we have an image and we need to convert it into histogram for GrayScale. We have several ways


# 1ST METHOD: Finding Histogram by matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)

#img = np.zeros([200,200], np.uint8)

#cv2.rectangle(img, (0, 100), (50,100), (255), -1)
#cv2.rectangle(img, (60, 80), (100,120), (127), -1)


cv2.imshow("Image", img)

# 1st argument is the source of image
# 2nd argument is the maximum number of pixel value
# 3rd argument is the range
plt.hist(img.ravel(), 256, [0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()