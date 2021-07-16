"""Hangman
Guess the letters to a secret word before the hangman is drawn."""

import random, sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# Play with changing CATEGORY and WORDS with new ones
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main():
    print('Hangman')
    
    # Set up variables for new game
    missedLetters = []  # List of incorrect letter guesses
    correctLetters = []  # List of correct letter guesses
    secretWord = random.choice(WORDS)   # The word the play must guess
    
    while True:    # Main game
        drawHangman(missedLetters, correctLetters, secretWord)
        
        # Let the player enter their letter guess
        guess = getPlayerGuess(missedLetters + correctLetters)
        
        if guess in secretWord:
            # Add the correct guess to correctLetters
            correctLetters.append(guess)
            
            # Check if the player has won
            foundAllLetters = True  # Start off assumin they've won
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                     # There's a letter in the secret word that isn't yet in correctLetters, so the play hasn't won
                     foundAllLetters = False
                     break
                if foundAllLetters:
                    print('Yes! the secret word is: ', secretWord)
                    print('You have won!')
                    break
                    
        else:
            # The player has guessed incorrectly
            missedLetters.append(guess)
            
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was " {} "'.format(secretWord))
                break
                
                
def drawHangman(missedLetters, correctLetters, secretWord):
 
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is: ', CATEGORY)
    print()
    
    # Show the incorrectly guessed letters
    print('Missed Letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()
    
    # Display the blanks for the secret word
    blanks = ['_'] * len(secretWord)
    
    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]
            
    # Show the secret word with spaces in between each letter
    print(' '.join(blanks))
    
def getPlayerGuess(alreadyGuessed):
 
    while True:
        print('Guess a letter. ')
        guess = input('> '.upper())
        if len(guess) != 1:
            print('Please enter a single letter. ')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter.  Choose again. ')
        elif not guess.isalpha():
            print('Please enter a LETTER. ')
        else:
            return guess
            
            
 # If this program was run (instead of imported), run the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
      sys.exit()    # When Ctrl-C is pressed, end the game