# Smoothing or Blurring is very important in image processing
# The most common kind of smoothing is to remove noise from images
# For smoothing and blurring, we use diverse-linear filters because they are relatively faster and easy to handle
# There are various filters like Homogeneous filters, Gaussian filters, median filters, bilateral filters
# In image processing, a kernel, convolution matrix or mask is a small matrix used for blurring, sharpening, embossing, edge detection and more
# In 1D signals, images also can be filtered with various Low-Pass Filters(LPF) or High-Pass Filters(HPF)
# LPF will remove the noise and blur the image
# HPF will helps in finding edges in images

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# We will create kernel 5x5 for image filtering using 2D convolution or homogeneous filter
kernel = np.ones((5,5), np.float32)/25
# 1ST ALGORITHM: Homogeneous Filter > most simple filter, each output pixel is the mean of its kernel neighbours
# 1st argument is the source that is image
# 2nd argument is the desired depth of destination image
# 3rd argument is the kernel
dst = cv2.filter2D(img, -1, kernel)

# For image blurring, we need to convolve over a image to a LPF kernel, we have some algorithms
# 2ND ALGORITHM: We use algorithm named Blur-Method or Averaging
# 1st argument is the source, 2nd is the kernel
blur = cv2.blur(img, (5,5))

# 3RD ALGORITHM: name Gaussian filter algorithm using different weight kernel in both x and y directions
# 1st argument is the source, 2nd is the kernel, 3rd is the Sigma X value
gblur = cv2.GaussianBlur(img, (5,5), 0)


# 4TH ALGORITHM: name Median filter algorithm, replaces each pixel with medians of its neighbouring pixels so called SALT & PEPPER NOISE
# Keep in mind Kernel size should be ODD but not 1, if 1 then gives original image
median = cv2.medianBlur(img, 5)

# 5TH ALGORITHM: name Bi-lateral Filter algorithm which retains sharp corners but can blur
# 2nd argument is the diameter of filter
# 3rd argument is the sigma color which is filter sigma in the color space
# 4th argument is the sigma space which is sigma filter in the coordinate space
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Image', '2D Convolution', 'Blur', 'Gaussian Blurring', 'Median', 'Bi-lateral Filter']
images = [img, dst, blur, gblur, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()

