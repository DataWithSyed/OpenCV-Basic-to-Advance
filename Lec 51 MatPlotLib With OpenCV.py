import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

cv2.imshow("Image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Opencv reads images in the form of BGR format
# Matplotlib reads image in the form of RBG format
# To see original image you need to convert RBG to BGR format
plt.imshow(img)

# this gonna hide the x, y tick values 
plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()