import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8') # 500x500 ve 3 channel renk RGB
#cv.imshow('Blank', blank)

# img = cv.imread('Photos/cat1.jpg')
# cv.imshow('Cat', img)

# 1. paint the image a certain colour
#blank[:] = 0,255,0 # : bütün pixelleri temsil ediyor
blank[200:300, 300:400] = 0,255,0 # : böyle de belirli bölgeleri boyuyabiliyoruz
#cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank,(0,0), (500,250), (0,255,0), thickness = 2) # Thickness -> stroke, blank.shape[1]//2, blank.shape[0]//2 -> height widthi alır ve ikiye böler
#cv.imshow('Rectangle', blank)

# 3. Draw a circle

cv.circle(blank, (250,250), 40, (0,0,255), thickness= 3)
#cv.imshow('Circle',blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness= 3)
#cv.imshow('Line',blank)

# 5. Write text
cv.putText(blank, 'Hello', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness= 2 )
cv.imshow('Text',blank)
cv.waitKey(0)