import cv2 as cv

img = cv.imread('shapes.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 3
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if 0.95 <= aspectRatio <= 1.05:
            cv.putText(img, 'Square', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))
        else:
            cv.putText(img, 'Rectangle', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_COMPLEX, .5, (0, 0, 0))

cv.imshow("shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()
