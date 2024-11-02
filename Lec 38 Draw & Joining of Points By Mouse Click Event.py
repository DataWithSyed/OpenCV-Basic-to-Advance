# Draw Points and Connect them through a line and can be used to join points in satellite tracking

import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (0,0,255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 3)
        cv2.imshow('Image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        points.clear()
        print(points)
img = np.zeros([512,512,3], np.uint8)
#img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)
points = []
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()