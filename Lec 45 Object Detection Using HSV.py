# HSV is also called the Hex-Cone Color Models and stands for Hue, Saturation & Value
# More than 150 color spaces in Opencv
# What is HSV color space?  It is used to separate image luminence from color information
# In RGB Color space, are all related to color luminence which means intensity

# Hue is the color components
# Saturation is the depth of color or intensity of any components
# Value is the brightness of color

import cv2
import numpy as np

def nothing(x):
    pass

#cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread('smarties.png')
    # Convert this reading image into HSV image for Image Tracking
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # we will threshold the HSV image for a range of Blue Color
    l_b = np.array([110, 50, 50])
    u_b = np.array([130,255,255])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()