import numpy as np
import cv2

# How can you create a image using numpy zeros method
#img = cv2.imread('lena.jpg', 1)

# 1st argument will be list height, width and
# 2nd argument will be data type
img = np.zeros([512, 512, 3], np.uint8)

# 1st argument is the image on which you want to draw the geometric shape
# 2nd argument deals with starting coordinates of point 1 that is top left starting coordinates
# 3rd argument is the ending coordinates of 2nd point that is bottom right ending coordinates
# 4th argument is the color of line. If you want to use different color then use   RGB COLOR PICKER
# 5th argument is the thickness of line

# for rectangle
img = cv2.rectangle(img, (50,50), (400,500), (0, 0, 255), 3)        # If there is -1 then it fills that color inside the shape

#for circle
img = cv2.circle(img, (55,86), 15, (255,0,255), 5)

# putting text on the image
# 1st argument is image you want to write
# 2nd argument is the text you want to write
# 3rd argument is the starting coordinates
# 4th argument is the font-face which requires a variable
font = cv2.FONT_HERSHEY_SIMPLEX
# 5th argument is the font size
# 6th argument is the color of text
# 7th argument is the thickness
# 8th argument is the line type
img = cv2.putText(img, 'OpenCV', (15,250), font, 4, (0,0,0), 10, cv2.LINE_AA)

cv2.imshow('Free', img)
cv2.waitKey()
cv2.destroyAllWindows()