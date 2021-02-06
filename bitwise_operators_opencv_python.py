import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
#img1 = cv2.rectangle(img1, (0, 0), (200, 500), (0, 0, 255), -1)
img1[:] = (0, 0, 255)
img2 = cv2.imread("baboon.jpg")
img2 = cv2.resize(img2, (500, 250))

bitAnd = cv2.bitwise_xor(img2, img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()
