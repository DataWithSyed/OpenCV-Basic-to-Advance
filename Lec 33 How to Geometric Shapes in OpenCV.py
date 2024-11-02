# Drawing Geometric shapes in OpenCV
import numpy as np
import cv2
img = cv2.imread('lena.jpg', 1)

# 1st argument deals with assistance of class
# 2nd argument deals with starting coordinates of point 1
# 3rd argument is the ending coordinates of 2nd point
# 4th argument is the color of line. If you want to use different color then use   RGB COLOR PICKER
# 5th argument is the thickness of line

img = cv2.line(img, (80,40), (80,400), (0,0,0), 3)    # for line
# img = cv2.arrowedLine(img, (80,0), (800,775), (255,0,0), 10)    # for arrowed line
img = cv2.line(img, (80,40), (400,40), (0,0,0), 3)

img = cv2.line(img, (400,40), (400,400), (0,0,0), 3)

img = cv2.line(img, (400,400), (80,400), (0,0,0), 3)

cv2.imshow('Hello', img)
cv2.waitKey()
cv2.destroyAllWindows()