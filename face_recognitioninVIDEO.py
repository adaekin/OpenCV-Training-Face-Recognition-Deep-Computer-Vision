import numpy as np
import cv2 as cv

cap = cv.VideoCapture('Videos/catvideo.mp4')
haar_cascade = cv.CascadeClassifier('FACEDETECTION/haar_face.xml')
people = ['anna', 'rte', 'sydney']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray , 1.1,3)
    
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+h]

        label, confidence = face_recognizer.predict(faces_roi)

        print(f'Label = {people[label]} with a confidence of {confidence}')
        cv.putText(frame, str(people[label]) + ' '+ str(int(confidence)), (x,y), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv.rectangle(frame, (x,y) , (x+w,y+h), (0,255,0), thickness= 2)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    cv.imshow('Gray Frame', frame)
cap.release()
cv.destroyAllWindows()
