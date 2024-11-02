# ROI stands for region of interest. Sometimes you need to work with certain location.
# i want to copy this football and paste in the image on other place
import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

# Return a tuple which contains number of rows, columns and channels
print(img.shape)

# return total number of pixels
print(img.size)

# return datatype of image. It is very useful in debugging the datatype
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# How to get coordinates of football
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()