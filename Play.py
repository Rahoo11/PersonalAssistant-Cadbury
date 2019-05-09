# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:46:41 2019

@author: MA389248
"""
import webbrowser
from Google import get_platform

def playSong(song):
    platform = get_platform()
    if platform=='Linux':
        chrome_path = '/usr/bin/google-chrome %s'
    elif platform=='OS X':
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform=='Windows':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = "https://www.youtube.com.tr/search?q={}".format(song)
    webbrowser.get(chrome_path).open(url)   