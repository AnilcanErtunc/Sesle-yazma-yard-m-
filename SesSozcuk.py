 #-*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:19:03 2020

@author: anilc
"""
def recognizer():
        import speech_recognition as sr
        sr.Microphone(device_index=1)

        r=sr.Recognizer()

        r.energy_threshold=5000

        with sr.Microphone() as source:
                
                audio=r.listen(source)
        try:
                text=r.recognize_google(audio,language="tr-TR")                
                return(format(text))

        except:
                return("Cant recognized")
