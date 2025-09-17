#BLURRING
import cv2 as cv

img = cv.imread('Photos/cat2.jpg')
cv.imshow('Image',img)
#Averaging -> pikselleri ortalar
average = cv.blur(img,(3,3))
cv.imshow('Average Blur', average)

#Gaussian Blur -> Daha doğal

gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur -> Helps to reduce noise
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#Bilateral -> Edge yumuşatır
bilateral = cv.bilateralFilter(img, 15, 35, 30)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)