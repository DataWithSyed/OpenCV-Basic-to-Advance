# Bitwise operations are very useful when dealing with mask
# Mask are binary images that indicates the pixel in which the operation is to be performed
import numpy as np
import cv2

img1 = np.zeros([240, 320, 3], np.uint8)
img1 = cv2.rectangle(img1, (200,0), (120, 160), (255,255,255), -1)

img2 = cv2.imread('LinuxLogo.jpg')

# How to perform bitwise operations are AND, OR NOT
#bitAnd = cv2.bitwise_and(img2, img1)
#bitOr = cv2.bitwise_or(img2,img1)
#bitXOr = cv2.bitwise_xor(img2,img1)

# NOT operation has only one attribute it gives inverse of result
bitNOT1 = cv2.bitwise_not(img1)
bitNOT2 = cv2.bitwise_not(img2)

# To save a picture
cv2.imwrite('Not.jpg', bitNOT2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

#cv2.imshow('Classy', bitAnd)
#cv2.imshow('Classy', bitOr)
#cv2.imshow('Classy', bitXOr)
cv2.imshow('Classy', bitNOT1)
cv2.imshow('Classy1', bitNOT2)

cv2.waitKey(0)
cv2.destroyAllWindows()