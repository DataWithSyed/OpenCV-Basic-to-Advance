

import cv2

img = cv2.imread('lena.jpg', 1)
cv2.imshow('Classy', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png', img)
# first argument will be image name
# 2nd argument is the image which you are trying to write