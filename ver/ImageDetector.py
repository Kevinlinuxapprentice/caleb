#!/usr/bin/env python3
import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_dafault.xml')

img = cv2.imread('marina.jpeg')

cv2.imshow('Clever programmer face detector', img)

cv2.waitKey()

print("deu certo")
