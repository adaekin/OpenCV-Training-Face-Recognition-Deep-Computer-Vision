import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat2.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45 , img.shape[0]//2 - 17), 100,255,-1)
cv.imshow('Mask', mask)

# maskRectangle = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255,-1)
# cv.imshow('Mask Rectange', maskRectangle)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)

# masked2 = cv.bitwise_and(img,img,mask=maskRectangle)
# cv.imshow('Masked Image Rectange', masked2)
cv.waitKey(0)