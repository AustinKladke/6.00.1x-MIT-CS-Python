# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    hangman_word = ""
    for i in secretWord:
        if i in lettersGuessed:
            hangman_word += i
        else:
            hangman_word += "_ "
    return hangman_word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    currently_available_letters = string.ascii_lowercase
    for i in lettersGuessed:
        if i in currently_available_letters:
            currently_available_letters = currently_available_letters.replace(i, "")
    return currently_available_letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # Beginning of game
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("-------------")
    
    letters_guessed = [] # Being used for letters guessed and for available letters
    guesses_left = 8
    # Loop that goes through each guessing round
    while guesses_left > 0:
        # Number of guesses that are left for the user to make
        print("You have {} guesses left.".format(guesses_left))
        
        # Print out available letters
        print("Available Letters: {}".format(getAvailableLetters(letters_guessed)))
        
        # User inputs a letter guess
        guess = input("Please guess a letter: ")
        guess_lowercase = guess.lower()
                
        # If the guess is already in letters_guessed, print out
        # that they've already guessed that letter
        if guess_lowercase in letters_guessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letters_guessed)))
            print("-----------")
            continue
        
        # Add letters guessed to the letters_guessed list,
        # if it is not already in the list
        if guess_lowercase not in letters_guessed:
            letters_guessed.append(guess_lowercase)
        
        # Decrement guesses left by 1 if guess is not in
        # the secret word
        if guess_lowercase not in secretWord and guess_lowercase in letters_guessed:
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, letters_guessed)))
            guesses_left -= 1
        
        # Show user what letters have been guessed so far
        # within the structure of the word
        else:
            print("Good guess: {}".format(getGuessedWord(secretWord, letters_guessed)))
        
        print("-----------")
        # If entire word has been guessed correctly, break out of the loop
        if isWordGuessed(secretWord, letters_guessed) == True:
            break
    if isWordGuessed(secretWord, letters_guessed) == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
