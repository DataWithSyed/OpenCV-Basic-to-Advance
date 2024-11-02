# For Basic Motion Detection and tracking
# I want to create a program which detect movement and give status of movement

import cv2
import numpy as np


cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2= cap.read()
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)

# We are converting frame into garyscale because of finding contours in the later stages
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # We are going to dilate the thresholded image to fill in all the holes which helps us finding contours
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Finding contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    for contour in contours:
        (x,y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.imshow('Feed', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
# remove these noises (for moving rope) and create rectangle around it


    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()