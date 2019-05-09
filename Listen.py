# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:14:56 2019

@author: MA389248
"""
import speech_recognition as sr
from Speech import speak

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        speak("I am sorry, I did not understand. Could you repeat it again?")
        return "error"
    except sr.RequestError as e:
        speak("I am sorry, I did not understand. Could you repeat it again?")
        return "error"

    return data
    