# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:10:50 2019

@author: MA389248
"""
import random
import time
from Listen import hear
from Speech import speak
def game():
     # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["apple", "banana", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    
    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    speak(instructions)
    #time.sleep(3)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            st = 'Guess {}. Speak!'.format(i+1)
            speak(st)
    
            guess = hear()
            if guess!="error":
                speak("You said: {}".format(guess))
                # determine if guess is correct and if any attempts remain
                guess_is_correct = guess.lower() == word.lower()
                user_has_more_attempts = i < NUM_GUESSES - 1
                break
            else:
                speak("Let's hear it again.")

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            st = "Correct! You win!"+ word
            speak(st)
            break
        elif user_has_more_attempts:
            speak("Incorrect. Try again.")
        else:
            st = "Sorry, you lose! I was thinking of '"+word+"'"
            speak(st)
            break