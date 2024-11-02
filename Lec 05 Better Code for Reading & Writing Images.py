# here we will make our program to destroy all windows when a person press ESC key without save it into new file
# When anyone press S key then we will save this image with the new name

import cv2

img = cv2.imread('baboon.jpg', 0)

cv2.imshow('Great Work', img)
k = cv2.waitKey(0) & OxFF
if k == 27:  # 27 means integer for ESC key
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Monkey.png', img)
    cv2.destroyAllWindows()
