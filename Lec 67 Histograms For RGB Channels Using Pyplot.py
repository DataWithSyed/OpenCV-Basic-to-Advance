# What are Histograms? A graph or a plot which gives you an overall idea about intensity distribution of an image
# Lets say we have an image and we need to convert it into histogram for RGB channels. We have several ways


# 1ST METHOD: Finding Histogram by matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg")

b, g, r = cv2.split(img)

cv2.imshow("Image", img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

# 1st argument is the source of image
# 2nd argument is the maximum number of pixel value
# 3rd argument is the range
plt.hist(img.ravel(), 256, [0,256])
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()