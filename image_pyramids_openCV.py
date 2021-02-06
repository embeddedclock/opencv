import cv2 as cv


img = cv.imread('lena.jpg')
layer = img.copy()
gp = [layer]

"""""
lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)
hr1 = cv.pyrUp(lr2)
cv.imshow("PyrDown Image1", lr1)
cv.imshow("PyrDown Image2", lr2)
cv.imshow("PyrUp Image", hr1)

"""""
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow((str(i)), layer)

layer = gp[5]
cv.imshow('upper level gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.imshow("Original Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
