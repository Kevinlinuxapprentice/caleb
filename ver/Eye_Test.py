#!/usr/bin/env python3
import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


webcam = cv2.VideoCapture('http://192.168.0.65:4747/video?640x480')

while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale( grayscaled_img )

    for (x,  y, w, h) in face_coordinates:
    
        cv2.rectangle(frame, (x, y), (x+w, y+h),  (0, 255, 0), 2)
    

    cv2.imshow('identificador de rostos', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break
#key = cv2.waitKey(1)

#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#face_coordinates = trained_face_data.detectMultiScale( icapture )

#print(face_coordinates)

#for (x,  y, w, h) in face_coordinates:
#    cv2.rectangle(img, (x, y), (x+w, y+h),  (0, 255, 0), 2)
#cv2.rectangle(img, (15, 110), (78, 78),  (0, 255, 0), 2)

#cv2.imshow('identificador de rostos', img)

#cv2.waitKey()

print("deu certo")
