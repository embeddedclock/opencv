import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=1)
erosion = cv.erode(mask, kernel, iterations=1)

titles = ['image', 'mask', 'dilation', 'erosion']
images = [img, mask, dilation, erosion]

for i in range(4):
    plt.subplot(1, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
