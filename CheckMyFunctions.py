'''
This module is for you to use to test your implemention of the functions in Hangman.py

@author: rodger
'''

import Hangman


if __name__ == '__main__':
    print('Testing createDisplayString')
    lettersGuessed = ['a', 'e', 'i', 'o', 's', 'u']
    misses = 4
    hangmanWord = list('s___oo_')
    s = Hangman.createDisplayString(lettersGuessed, misses, hangmanWord)
    print(s)
    print()

    print('Testing updateHangmanWord')
    guessedLetter = 'a'
    secretWord = 'cat'
    hangmanWord = ['c', '_', '_']
    expected = ['c', 'a', '_']
    print('Next line should be: ' + str(expected))
    print(Hangman.updateHangmanWord(guessedLetter, secretWord, hangmanWord))