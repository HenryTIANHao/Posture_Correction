import cv2 as cv

img = cv.imread("front_new.jpg")
img = cv.resize(img, None, fx=0.25, fy=0.25)
cv.imwrite('front_new_pre.jpg', img)
