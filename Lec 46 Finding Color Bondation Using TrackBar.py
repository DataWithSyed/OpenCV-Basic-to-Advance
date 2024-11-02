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

cv2.namedWindow("Tracking")
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)

cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    frame = cv2.imread('smarties.png')
    # Convert this reading image into HSV image for Image Tracking
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LH", 'Tracking')
    l_s = cv2.getTrackbarPos("LS", 'Tracking')
    l_v = cv2.getTrackbarPos("LV", 'Tracking')

    u_h = cv2.getTrackbarPos("UH", 'Tracking')
    u_s = cv2.getTrackbarPos("US", 'Tracking')
    u_v = cv2.getTrackbarPos("UV", 'Tracking')
    # we will threshold the HSV image for a range of Blue Color
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()