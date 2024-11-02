# What is Template Matching? It is a method of finding and searching the location of a template image inside a larger image


import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('messi-small.png', 0)

# 1st argument is the image
# 2nd is the template you want to find in your image
# 3rd argument is the method of template matching
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

#print(res)
w, h = template.shape[::-1]


# Finding the brightest point in the image
threshold = 0.15835
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()