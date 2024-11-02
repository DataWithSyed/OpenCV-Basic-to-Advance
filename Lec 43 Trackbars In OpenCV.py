# Track-bars are very useful to change any value on images dynamically in run time
# I want to change BGR Channel of image using this Track-bar

import numpy as np
import cv2

# create a black image, a window
img = np.zeros([300, 512, 3], np.uint8)

# To name a window you created
cv2.namedWindow('Image')

def nothing(x):
    print(x)

# 1st argument is the name of the track-bar
# 2nd argument is the name of the window
# 3rd argument is the initial value at which your track-bar is initially set
# 4th argument is the count which means final value of your track-bar
# 5th argument is the callback function which will be called whenever your track-bar value changes
cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('R', 'Image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while (1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
# Value for ESC key is 27
    if k == 27:
        break
# To get the position of the set channels for track-bar
    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else:
        #  To set current bgr channel value to the img variable
        img[:] = [b, g, r]

cv2.destroyAllWindows()