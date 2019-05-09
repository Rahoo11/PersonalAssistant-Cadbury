# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:07:53 2019

@author: MA389248
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Speech import speak
from Listen import hear
from Game import game
import time, datetime
from Play import playSong
from Google import google,google_search,maps
import feedparser

def cadbury(data):
    """
    Searches the input string for keywords, or commands.
    If keywords are found, it calls appropriate function.
    List of functions:
    (1) Open maps for a place
    (2) Play Game
    (3) Tell the time.
    (4) Google, or search for a string online.
    (5) Open Google
    (6) Play Song on Youtube
    (7) Reading News feed 
    """
    #Splitting each sentence in a list of words.
    word_list = word_tokenize(data)
    
    #Setting up stop_words: words that are redundant.
    stop_words = set(stopwords.words('english'))

    #Creating space for a list of sentences without stop_words.
    if "search" not in word_list and "google" not in word_list and "Search" not in word_list and "Google" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
        filtered_sentence = [w for w in word_list]
    
    if ("bored" in filtered_sentence):
        speak("Let's play a game then!!")
        game()
    elif 'time' in filtered_sentence:
        speak(time.strftime("%A") + " "+ str(datetime.datetime.now())[:16])    
    elif 'song' in filtered_sentence and filtered_sentence.index('play') < filtered_sentence.index('song'):
        filtered_sentence = [w for w in filtered_sentence if w != "called" and w != "named" and w != "titled"]
        pos = filtered_sentence.index('song') + 1
        speak("Opening Youtube Searches for {}".format(filtered_sentence[pos]))
        playSong(filtered_sentence[pos])  
    elif 'game' in filtered_sentence and filtered_sentence.index('play') < filtered_sentence.index('game'):
        game()
    elif 'google' in filtered_sentence or "Google" in filtered_sentence:
        if len(filtered_sentence) > 1:
            if 'open' in filtered_sentence and 'google' in filtered_sentence and filtered_sentence.index('open') < filtered_sentence.index('google'):
                google()
            if 'open' in filtered_sentence and 'Google' in filtered_sentence and filtered_sentence.index('open') < filtered_sentence.index('Google'):
                google()
            else:
                pos = 0
                if 'google' in filtered_sentence:
                    pos = filtered_sentence.index('google') + 1
                elif 'Google' in filtered_sentence:
                    pos = filtered_sentence.index('Google') + 1
                if 'word' in filtered_sentence and filtered_sentence[-1] != 'word':
                    filtered_sentence =[w for w in filtered_sentence if w != "word"]

                search_string = ''.join(filtered_sentence[pos:])
                google_search(search_string)
        else:
            speak("If you want me to open google, say 'open google'")
            speak("If you want me to search for a word,"
                "say 'google <word>'")
    elif 'search' in filtered_sentence:
        if filtered_sentence[-1] == "search":
            speak("What would you like me to search?")
            for j in range(5):
                search_string = hear()
                if(search_string!='error'):
                    google_search(search_string)
                    break
            return None
        pos = filtered_sentence.index('search') + 1
        search_string = " ".join(filtered_sentence[pos:])
        google_search(search_string)
    elif 'location' in filtered_sentence:
        if filtered_sentence[-1]=="location":
            speak("What place should I look for?")
            for j in range(5):
                location = hear()
                if(location!="error"):
                    maps(location)
                    break
            return None
           
        pos = filtered_sentence.index('location')+1
        loc = "".join(filtered_sentence[pos:])
        maps(loc)
    elif 'news' in filtered_sentence:
        speak("Here are the top 5 stories for you.")
        NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
        for j in range(5):
            entry = NewsFeed.entries[j]
            speak("Number {}".format(j+1))
            speak(entry.title)
            speak(entry.summary)
            print("=======================================")
    else:
        speak("I am not aware of this command. Could you try something else?")
    return None  
        