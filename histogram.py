import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat2.jpg')

cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure() # Grinin gücünün pixele oranı tablosu
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Color Histogram
plt.figure() # Color gücünün pixele oranı tablosu
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)