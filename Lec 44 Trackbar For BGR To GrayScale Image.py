# Just use 2 trackbar to change bgr image into grey scale image
import numpy as np
import cv2

cv2.namedWindow('Image')

def nothing(x):
    print(x)
cv2.createTrackbar('CP', 'Image', 10, 400, nothing)

# Swtich is for changing grey scale to BGR image or vice versa
switch = 'Color/Gray'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while (1):
    img = cv2.imread('messi5.jpg')

    pos = cv2.getTrackbarPos('CP', 'Image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (10,70), font, 1, (0,0,255), 3)

    k = cv2.waitKey(1) & 0xFF
# Value for ESC key is 27
    if k == 27:
        break
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        pass
    else:
        #  To set current bgr channel value to the img variable
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('Image', img)
cv2.destroyAllWindows()