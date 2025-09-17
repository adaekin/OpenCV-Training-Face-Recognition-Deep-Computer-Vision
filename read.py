import cv2 as cv


img = cv.imread('Photos/cat1.jpg')


def rescaleFrame(frame, scale=0.75): # for pictures, videos, live videos
    width = int(frame.shape[1]*scale) #frame shape 1 is width
    height = int(frame.shape[0] * scale) #frame shape 0 is height
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height): # only for videos
    capture.set(3,width) # 3 is width
    capture.set(4,height) # 4 is height

resized_image = rescaleFrame(img)
cv.imshow("Image", img)
cv.imshow("Image Resized", resized_image)


capture = cv.VideoCapture('Videos/catvideo.mp4') # video capture yerine 0,1 yazıp kamerayı kullanabiliyoruz

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
