import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]

img[273:333, 100:160] = ball

# It can resize your image
# 1st argument is the image or data you want to resize
# 2nd argument is the rows and columns in the form of tuple
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

# You can only add two images when they have same size
# dst = cv2.add(img, img2)

# it will increase/decrease the opacity of images
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
