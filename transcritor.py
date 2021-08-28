#!/usr/bin/env python3
import os
import sys
import speech_recognition as sr
import decisao

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("diga algo ai...")

        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio).lower()
            print("vc disse : \n " , r.recognize_google(audio))
            f = open("audiorecording.txt", "a")
            f.write(r.recognize_google(audio))
            f.close()
            decisao.escolhendoComando(comando)

        except Exception as e:
            print("erro: " , str(e))

if __name__=="__main__":
    main()
