"""Crack the code!
A deductive logic game where you must guess the series of numbers based on feedback."""

import random

NUM_DIGITS = 4
MAX_GUESSES = 10

def main():
  print('''Crack the code! Can you crack the code before your guesses run out?
  
  The code consist of a {}-digit number with no repeated digits.
  Try to guess the number, while the feedback will hint you in the right direction
  Feedback displayed:       Means:
    Getting Warm!           One number is correct but in the wrong place.
    Close!!                 One number is correct and it is in the right place.
    Very Cold!!!            No numbers are correct.
    
  Good Luck!'''.format(NUM_DIGITS))
  
      while True: # Main game
        secretNum = getSecretNum()
        print('I have come up with a combination of numbers. ')
        print(' You have {} guesses to crack the code!.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numbGuesses))
                guess = input ('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of trys. ')
                print('The answer was {}. '.format(secretNum))
                
         # Ask to play again
         print('Do you want play again? (Type Yes or No) ')
         if not input ('> ').lower().startswith('y'):
            break
      print('Thank you for playing, see you soon! ')
      
      
def getSecretNum():
      numbers = list('0123456789')
      random.shuffle(numbers)
      
      secretNum = ''
      for i in rang(NUM_DIGITS):
          secretNum += str(numbers[i])
      return secretNum
      
      
def getClues(guess, secretNum):
      if guess == secretNum:
          return 'You cracked it!'
          
      clues = []
      
      for i in range(len(guess)):
          if guess[i] == secretNum[i]:
              # correct number is in the right place
              clues.append('Close!!')
           elif guess[i] in secretNum:
              # correct number is in the wrong place
              clues.append('Getting Warm!)
      if len(clues) == 0:
          return 'Very Cold!!!'  # There are no correct numbers
      else:
          clues.sort()
          return ' '.join(clues)
          
          
# If the program is run (instead of imported), run the game
if  __name__  == '__main__':
    main()
