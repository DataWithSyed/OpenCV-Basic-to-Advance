# What is canny edge detector? It is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images
# Canny Edge Detection Algorithm is divided into 5 steps:
# 1. Noise Reduction  >  It will smooth the image apply Gaussian Filter
# 2. Gradient Calculation  >  Find Intensity gradients
# 3. Non-maximum Suppression  >  To get rid of spurriers response to edge detection
# 4. Double Threshold  >  apply double thresholding to determines potential edges
# 5. Edge Tracking By Hysteresis  >  to finalize the detection of the edges by suppressing all the other edges that are weak or not connected to strong edges


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1st argument is the source of image
# 2nd & 3rd argument is the First & Second Threshold value for hysteresis procedure
canny = cv2.Canny(img, 50, 250)

titles = ['Image', 'Canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()