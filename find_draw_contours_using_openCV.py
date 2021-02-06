import cv2 as cv

img = cv.imread('opencv-logo.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(cv.THRESH_BINARY)
ret, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow('original', img)
cv.imshow('gray', img_gray)
cv.imshow('binary', img_binary)
cv.waitKey(0)
cv.destroyAllWindows()
