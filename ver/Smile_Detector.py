#!/usr/bin/env python3

import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
trained_smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

webcam = cv2.VideoCapture('http://192.168.0.65:4747/video?640x480')


while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale( grayscaled_img )
    smile_coordinates = trained_smile.detectMultiScale(grayscaled_img)


    for (x,  y, w, h) in face_coordinates:

        cv2.rectangle(frame, (x, y), (x+w, y+h),  (0, 255, 0), 2)
    for (x,  y, w, h) in smile_coordinates:

        cv2.rectangle(frame, (x, y), (x+w, y+h),  (0, 0, 255), 2)


    cv2.imshow('identificador de rostos', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()

print("deu certo")
