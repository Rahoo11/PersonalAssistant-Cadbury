# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:01:09 2019

@author: MA389248
"""

import time
from Speech import speak
from Cadbury import cadbury
from Listen import hear


def main():
    time.sleep(2)
    speak("Hello! What can I do for you today?")
    while 1:
        data = hear()
        exit_flag = 0
        #data = input();
        if data!="" and data!="error":
            if "bye" in data:
                speak("Bye, Have a great day!")
                break
            if "cadbury"==data or "Cadbury"== data:
                speak("Yes right! That's my name. Tell me how may I help you?")
            else:
                cadbury(data)
                time.sleep(5)
                speak("Do you have any other commands?")
                for j in range(5):
                    confirm = hear()
                    if "error" not in confirm and "yes" not in confirm:
                        exit_flag=1
                        break
                    elif "yes" in confirm:
                        exit_flag=0
                        break
                if exit_flag == 1:
                    speak("Okay then. My work here is done. Have a good day!!")
                    break
                else:
                    speak("Great!!What can I do for you next?")
               
if __name__ == "__main__":
    main()


