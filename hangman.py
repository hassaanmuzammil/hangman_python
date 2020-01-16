# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        #if len(secret_word) == len(letters_guessed):
        if letter not in letters_guessed:
            return False                               
    return True
            


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    letters_guessed = ['a','b','c','d']
#    secret_word = 'ebadcdef'
#    print(len(secret_word))
#    print(len(letters_guessed))
    i = 0
    guessed_word = ['','','','','','','','','','','','','','','']
    for letter in secret_word:
        if letter in letters_guessed:    
            guessed_word[i] = letter
            i += 1
        else:      
            guessed_word[i] = "_ "
            i +=1
        
    print(''.join(guessed_word), end='' )



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
             available_letters.append(letter)
             
    print("Available Letters: " + " ".join(available_letters))



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
#secret_word = 'apple'
    letters_guessed = []
    guesses_remaining  = 6
    print("Letters in secret word: ", len(secret_word))
    while guesses_remaining > 0:
        print("\n")
#        draw_hangman(guesses_remaining)
        get_available_letters(letters_guessed)
        print("Guesses Remaining: ", guesses_remaining)
        get_guessed_word(secret_word,letters_guessed)
        guessed_char = input("Guess a character: ")
        letters_guessed.append(guessed_char)
        print(letters_guessed)
        if is_word_guessed(secret_word,letters_guessed) == True:
            get_guessed_word(secret_word,letters_guessed)
            break       
        if guessed_char in secret_word:
            print("Well guessed")
#            get_guessed_word(secret_word,letters_guessed)
        else:
            print("Wrong guess!")
            guesses_remaining -= 1
#            get_guessed_word(secret_word,letters_guessed)
        draw_hangman(guesses_remaining)
        
    if is_word_guessed(secret_word,letters_guessed) == False:
         print("\nNo more guesses remaining\n")
         print("Hanged! Better luck next time!")
         print("The correct word was: ",secret_word)
    else:
         print("\nWell done! You guessed the word correctly.")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def draw_hangman(guesses_remaining):
    if guesses_remaining == 6:
        print("\t|---------")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")

    elif guesses_remaining == 5:
        print("\t|---------")
        print("\t|    | ")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")

    elif guesses_remaining == 4:
        print("\t|---------")
        print("\t|    | ")
        print("\t|    O ")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")

    elif guesses_remaining == 3:
        print("\t|---------")
        print("\t|    | ")
        print("\t|    O ")
        print("\t|    | ")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")

    elif guesses_remaining == 2:
        print("\t|---------")
        print("\t|    | ")
        print("\t|    O ")
        print("\t|    | ")
        print("\t|   / \\")
        print("\t|")
        print("\t|")
        print("\t|")

    elif guesses_remaining == 1:
        print("\t|---------")
        print("\t|    | ")
        print("\t|    O ")
        print("\t|    | ")
        print("\t|   / \\")
        print("\t|    | ")    
        print("\t|")
        print("\t|")


    else:
        print("\t|---------")
        print("\t|    | ")
        print("\t|    O ")
        print("\t|    | ")
        print("\t|   / \\")
        print("\t|    | ")    
        print("\t|   / \\")
        print("\t|\n")


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


def main():
    
    
    secret_word = choose_word(wordlist)
    print("Welcome to the game Hangman!")
    print(secret_word)
    hangman(secret_word)
    


if __name__ == "__main__":
    
    main()
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.


###############
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
