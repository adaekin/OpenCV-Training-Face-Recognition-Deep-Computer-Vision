import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat6.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 175,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny ,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # Contours -> list of cordinates of contours, Hierarchies -> shapes
print(f'{len(contours)} contour(s) found')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)