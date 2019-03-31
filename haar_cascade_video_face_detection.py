import cv2
import face_recognition
import numpy
cap=cv2.VideoCapture("/home/piyush/faces.mp4")

face_cascade=cv2.CascadeClassifier("/home/piyush/haarcascade_frontalface_default.xml")
while True:
    ret,frame=cap.read()
    gray_imag=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_imag,1.5,5)
    for x,y,w,h in faces:
        print(x,y,w,h)
        color=(255,0,0)
        stroke=2
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)

    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
