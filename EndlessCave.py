"""Endless Cave
Animation of a endless cave that goes on forever."""

import random, sys, time

# constants
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Endless Cave')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Display the tunnel segment
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    
    # Check for Ctrl-C press during the brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()     # When Ctrl-C is pressed, end the program
        
     # Adjust the left side width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
      leftWidth = leftWidth - 1   # Decreases left side width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
      leftWidth = leftWidth + 1   # Increase left side width
    else:
      pass   # Do nothing, no change in left side width
        
     # Adjust the gap width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
      gapWidth = gapWidth -1    # Decrease gap width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
      gapWidth = gapWidth + 1   # Increase gap width
    else:
      pass    # Do nothing, no change in gap width
