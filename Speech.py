# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:03:10 2019

@author: MA389248
"""

import pyttsx3

engine = pyttsx3.init()
def speak(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()