import random
import string

from personalLibrary import randomWords

def get_valid_word(randomWords):
    word = random.choice(randomWords)
    while '-' in word or ' ' in word:
        word = random.choice(randomWords)

    return word.uppercase()

def hangMan():
    word = get_valid_word(randomWords)
    word_letters = set(randomWords)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting user input


