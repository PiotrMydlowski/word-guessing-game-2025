# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 22:07:42 2025

@author: PIOTR
"""


import random


WORDS = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
TURNS_LIMIT = 10


def choose_random_word(words: str)->str:
    """
    Chooses a random word.
    """
    word = ''
    word = random.choice(words)
    return word


def play_game(word: str):
    """
    Guides player through one game.
    """
    
    turns_left = TURNS_LIMIT
    
    while True:

        player_input = str(input('Try to guess the word:'))
        
        if(player_input == word):
            print("That's it. You have won.")
            return
        
        elif(player_input in word):
            print('It is within a searched word.')
            
        else:
            print('Wrong.')
        
        turns_left = turns_left - 1 #checking the turns limit
        if(turns_left < 0):
            print ('You have lost!')
            return
        else:
            print('You have {} turn(s) left.'.format(turns_left))
        
        
def ask_to_play_again()->bool:
    """
    Asks player if they want to play again.
    """
    
    while True:
        try:
            player_input = int(input('Input 1 to play again and 0 to exit: '))
            
            if(player_input == 1):
                return True

            elif(player_input == 0):
                return False

            else:
                print('This is not a valid choice.')
            
        except:
            print('This is not a number.')
        
        
    return False


def main():
    """
    Main function.
    """
    
    word = ''
    play_again = True
    
    print('Welcome to word guessing game.')
    
    while play_again:    
        word = choose_random_word(WORDS)

        play_game(word)
        
        play_again = ask_to_play_again()
    


main()