#I want to blend or merge these 2 images
# I want to blend right-half of orange to left-half of apple

import cv2
import numpy as np

# Step 01: Loading of images
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

# 1ST METHOD: produce both half images and stick together
apple_orange = np.hstack((apple[:, : 256], orange[:, 256:]))
cv2.imshow("Apple-Orange", apple_orange)

# 2ND METHOD: use image PYRAMID TECHNIQUES to blend these images
# To blend images by Pyramid techniques, we need to follow 5 steps:
# 1. Load the images
# 2. Find the Gaussian pyramids for apple and orange (in this example, no. of levels is 6)
# 3. From Gaussian pyramids, find their laplacian pyramids
# 4. Now join the left-half of apple and right-halp of orange in each level of laplacian pyramids
# 5. Finally from this joint image pyramids, reconstruct the original image

# Step 02: generation of gaussian pyramid
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Step 03: Generation of Laplacian pyramid
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# Step 04: Join the both halves of images
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Step 05: Reconstruct Image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('Apple-Orange-Reconstruct', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()