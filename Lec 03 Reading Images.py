# To write first code you need to install opencv packages go to file > then settings > then projects > then project interpreter then
#  > then click on plus button then write opencv-python and install it
# in this you will learn how to read  images

import cv2

img = cv2.imread('lena.jpg', 0)
# there are 2 arguments first one is name of file and the second argument has 3 flag 1, 0, -1

print(img) # if got none then you have choosen a wrong path

cv2.imshow('Classy', img)
# first argument will show the name of the window on which pic will display
# second argument contains the image which you call through imread method
cv2.waitKey(5000)
# this will show the image for 5000 milliseconds. If you chose waitKey(0) the window will wait for you to close window
cv2.destroyAllWindows()
# this will close all windows which you open through program Another Method: cv2.destroyWindow() for particular window
