# Mouse Click Event can be anything like right or left click mouse event
import cv2
import numpy as np

# to check the number of events
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# We will create a mouse callback function which is executed when a mouse event take place
# x, y are coordinates of the point at which we click
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText (img, strXY, (x, y), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # Here i want to print BGR channel where ever i click. Channel for blue=0 green=1  red=2
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)

# img = np.zeros([512,512,3], np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)

# this function will be use to call back the function which we just created
# 1st argument is the window name
# 2nd argument will be callback function
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()