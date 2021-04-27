'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Phillip Kang    pdk15
'''
import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    mode = input('Hard (8 misses) or Easy (8 misses) | (e or h?)> ')
    if mode == 'e':
        return 12
    if mode == 'h':
        return 8

def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    lst_words = []
    for i in words:
        if len(i) == int(length):
            lst_words.append(i)
        else:
            pass
    return random.choice(lst_words)

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    
    space = ' '.join(sorted(lettersGuessed))
    misses_left = str(missesLeft)
    hangman = ' '.join(hangmanWord)
    line1 = r"letters you've guessed: " + space + '\n'
    line1+= r"misses remaining = " + misses_left + '\n'
    line1+= hangman
    return line1
    pass

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)
    letter = input("letter> ")
    occur = 0
    while occur == 0:
        if letter not in lettersGuessed:
            occur += 1
            return letter
        else:
            print("you already guessed that")
            letter = input("letter> ")

def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    for i in range(len(secretWord)):
        if secretWord[i] == guessedLetter:
                hangmanWord[i] = guessedLetter
                secretWord = secretWord[:i] + '!' + secretWord[i+1:]
        else:
            pass
    return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    before = hangmanWord[:]
    updated = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    if before == updated:
        missesLeft -= 1
        return [updated, missesLeft, False]
    elif before != updated:
        return [updated, missesLeft, True]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    word_length = random.randrange(5, 10)
    missesLeft = handleUserInputDifficulty()
    missesTotal = missesLeft
    text = open(filename, 'r')
    file = text.readlines()
    secretWord = getWord(file, word_length)
    text.close()
    hangmanWord = (word_length - 1) * ['_']
    lettersGuessed = []
    while missesLeft > 0 and '_' in hangmanWord:
        displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(guessedLetter)
        guess = processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)
        if guess[-1] == False:
            print('The letter, ' + guessedLetter + ' was not in the word')
            missesLeft -= 1
    if '_' not in hangmanWord:
        print("You correctly guessed " + secretWord)
        amount = missesTotal - missesLeft
        print("You guessed " + str(len(lettersGuessed)) + " times with " + str(amount) + " misses")
        return True
    else:
        print("You're hung!!")
        print("Word is " + secretWord)
        amount = missesTotal - missesLeft
        print("You guessed " + str(len(lettersGuessed)) + " times with " + str(amount) + " misses")
        return False

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game,a which is done by calling runGame, therefore, we have provided you this code below.
    '''
    losses = 0
    wins = 0
    proceed = True
    while proceed == True:
        game = runGame('lowerwords.txt')
        if game == True:
            wins += 1
        else:
            losses += 1
        if input("Would you like to play again? | y or n> ") == 'n':
            print("You won " + str(wins) + " game(s) " "and lost " + str(losses))
            proceed = False
