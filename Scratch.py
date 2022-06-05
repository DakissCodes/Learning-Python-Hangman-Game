
# HANGMAN PROJECT
# LIST OF WORDS
# NUMBER OF LIVES : 6
# STEP 1: HAVE A FUNCTION THAT PRINTS THE HANGMAN BASED ON THE NUMBER OF LIVES
# STEP 2: A FUNCTION THAT PROMPTS AN INPUT FROM THE PLAYER (ONLY ALPHABETS)
# STEP 3: A FUNCTION THAT CHECKS WHETHER THE INPUT IS IN THE WORD (LIST)
# STEP 4: A FUNCTION THAT REPLACES '_' INTO ITS WORD
# NOTE: THERE SHOULD BE NO SPACES OF WORDS

import string
from random import choice
words = ['justine','rey','daquis']

def display_hangman(lives):

    man_dict = {1:'_______', 2:'|', 3:'|  O', 4:'| _O', 5:'| _O_', 6:'|  |', 8:'| (', 9:'| ( )'} 
    lives_dict = {6:[1,2,2,2], 5:[1,3,2,2],4:[1,4,2,2],3:[1,5,2,2],2:[1,5,6,2],1:[1,5,6,8],0:[1,5,6,9]}
    # we have different displays for different lives
    # different patterns for different lives
    for _ in lives_dict[lives]:
        print(man_dict[_])
     # head gets misaligned because of blank when mask[2] is missing

def user_prompt(alphabets,lives):
    user = '  '
    while user.upper() not in string.ascii_uppercase or len(user) != 1:
        print('\nAvailable letters: ' + '[' + ' , '.join([_ for _ in alphabets]) + ']')
        print(f'\nYou have {str(lives)} lives left!')
        user = input("\nGuess a letter: ")

        if user.isdigit():
            print('Input not in Letters!')
        if len(user.upper()) > 1:
            print('Only 1 letter!')
    return user.upper()

def letter_in_word(word,letter):
    if letter in word:
        return True,word.index(letter)
    return False, None
    # returns an index and bool

def word_printer(word):
    display = []
    for _ in range(len(word)):
        display.append('_')

display = []
def display_word(word,display):
    for _ in range(len(word)):
        display.append('_')
 # Create a function that gives hints

def filler(word,display):
    letters = [_.upper() for _ in word[::3]]
    for _ in letters:
        display[word.index(_)] = _


    





