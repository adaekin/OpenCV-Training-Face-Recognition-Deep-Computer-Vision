import cv2 as cv

img = cv.imread('Photos/cat2.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold,thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded', thresh)

threshold,thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresholded Inverse', thresh_inv)

# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)