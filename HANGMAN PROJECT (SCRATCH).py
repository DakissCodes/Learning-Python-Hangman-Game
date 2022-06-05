import random
import os
import time
import string
import Scratch

words = ['Accountant'] # INSERT WORD LIST HERE!

game = True
while game:
    lives = 6
    word = list(random.choice(words).upper())
    alphabets = list(string.ascii_uppercase)
    display = []
    Scratch.display_word(word, display)
    Scratch.filler(word,display)
    while lives > 0 and display.count('_') != 0:
        Scratch.display_hangman(lives)
        print(' '.join(display))  
        letter = Scratch.user_prompt(alphabets,lives)
        if (letter in word and letter not in display) or (letter in word and letter in display and word.count(letter) > display.count(letter)):

            alphabets.pop(alphabets.index(letter))
            index_list = [x for x,y in enumerate(word) if y.upper() == letter.upper()] # returns the indexes of the same letter
            for _ in index_list:
                display[_] = letter
            print('\nCorrect letter!')
            
            time.sleep(.5)
            os.system('cls')

        else:
            lives -= 1
            if letter not in word: print(f'\nLetter not in word! You have {lives} LIVES left!')
            elif letter in display: print('\nLetter already in word!')
            time.sleep(.5)
            os.system('cls')

    if lives == 0 and display.count('_') > 0:
        print('\nYou lost the game!')
        Scratch.display_hangman(lives)
        print("\nThe word was: " + ''.join([_.upper() for _ in word]))

    else:
        print('You have won the game!')
        print('\n')
        Scratch.display_hangman(lives)

    play_again = '1'
    while play_again.upper() not in 'YES NO': play_again = input('\nWould you like to play again [Y/N]:')
    if 'Y' in play_again.upper(): game = True
    else: game = False




