import cv2;

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=5)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        cv2.putText(frame,  'face detection test',  (50, 50),  font, 1, (0, 255, 0),3,cv2.LINE_4) 
    cv2.imshow('Test', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()