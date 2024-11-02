import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorimage = np.zeros([512,512,3], np.uint8)
        mycolorimage[:] = [blue, green, red]

        cv2.imshow('Color', mycolorimage)
#img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)

points = []

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()