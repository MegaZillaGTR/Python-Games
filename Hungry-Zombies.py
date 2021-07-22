"""Hungry Zombies!
Escape the Zombie hord by making them eat each other."""

import random, sys

WIDTH = 40
HEIGHT = 20
NUM_ZOMBIES = 10
NUM_TELEPORTS = 2
NUM_DEAD_ZOMBIE = 2
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = 'P'
ZOMBIE = 'Z'
DEAD_ZOMBIE = 'X'

WALL = chr(9617)    # Character 9617 is a uniqe character design

def main():
    print('''Hungry Zombies
    
    You are trapped in a maze with hungry zombies! You do not want to be eaten.  The zombies do not have functionaly thinking, so they will run into walls.
    
    You must trick the zombies into eating each other without being eaten yourself.  You have a personal teleporter device, but it has enough battery for {} trips.
    
    Zombies can go through the corners of two diagonal walls.  Stay safe!""".format(NUM_TELEPORTS))
    
    input('Press Enter to begin...''')
    
    #Set up a new game
    board = getNewBoard()
    zombies = addZombies(board)
    playerPosition = getRandomEmptySpace(board, zombies)
    while True:    # Main game
        displayBoard(board, zombies, playerPosition)
        
        if len(zombies) == 0:  # Check if the player has won
            print('All the zombies have eaten each other and you live to tell the tale!')
            sys.exit()
            
        # Move the player and zombies
        playerPosition = askForPlayerMove(board, zombies, playerPosition)
        zombies = moveZombies(board, zombies, playerPosition)
        
        for x, y in zombies:    # Check if the player has lost
            if (x, y) == playerPosition:
                displayBoard(board, zombies, playerPosition)
                print('You have been eaten!')
                sys.exit()
                
                
def getNewBoard():

    board = {'teleports': NUM_TELEPORTS}
    
    # Create an empty board
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE 
            
    # Add walls on the edges of the board
    for x in range(WIDTH):
        board[(x, 0)] = WALL    # Make top wall
        board[(x, HEIGHT -1)] = WALL    # Make bottom wall
    for y in range(HEIGHT):
        board[(0, y)] = WALL     # Make the left wall
        board[(WIDTH - 1, y)] = WALL    # Make the right wall
        
    # Add the random walls
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL
        
    # Add the starting dead zombies
    for i in range(NUM_DEAD_ZOMBIES):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ZOMBIES
    return board
    
    
def getRandomEmptySpace(board, zombies):

    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, zombies):
            break
        return(randomX, randomY)
        
        
def isEmpty(x, y, board, zombies):

    return board[(x, y)] == EMPTY_SPACE and (x, y) not in zombies
    
    
def addZombies(board):

    zombies = []
    for i in range(NUM_ZOMBIES):
        x, y = getRandomEmptySpace(board, zombies)
        zombies.append((x, y))
    return zombies
    
    
def displayBoard(board, zombies, playerPosition):
    # Display the board, robots, and player on the screen
    # Loop over every space on the board
    for y in range(HEIGHT):
        # Draw appropriate character
        if board[(x, y)] == WALL:
            print(WALL, end=' ')
        elif board[(x, y)] == DEAD_ZOMBIES:
            print(DEAD_ZOMBIES, end=' ')
        elif board[(x, y)] == playerPosition:
            print(PLAYER, end=' ')
        elif board[(x, y)] == zombies:
            print(ZOMBIE, end=' ')
        else:
            print(EMPTY_SPACE, end=' ')
    print()
    
    
def askForPlayerMove(board, zombies, playerPosition):

    playerX, playerY = playerPosition
    
    # Find which directions aren't blocked by a wall:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, zombies) 
    else:
    
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, zombies) else:
    
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, zombies) else:
    
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, zombies) else:
    
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, zombies) else:
    
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, zombies) else:
    
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, zombies) else:
    
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, zombies) else:
    
    allMoves = (q + w + e + d + c + x + a + z + 'S')
    
    while True:
        # Get player's move
        print('Teleports remaining: {} '.format(board["teleports"]))
        print('                     ({})  ({})  ({}) '.format(q, w, e))
        print('                     ({})  (S)   ({}) '.format(a, d))
        print('Enter move or QUIT:  ({})  ({})  ({}) '.format(z, x, c))
        
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # Teleport the player to a random empty space
            board['teleports'] -= 1
            return getRandomEmptySpace(boad, zombies)
        elif move != '' and move in allMoves:
            # Return the new player position based on their move
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)} [move]
                    
                    
def moveZombies(board, zombiePositions, playerPosition):

  playerx, playery = playerPosition
  nextZombiePositions = []
  
  while len(zombiePositions) > 0:
      zombiex, zombiey = zombiePosition[0]
      
      # Determine the direction the zombie moves
      if zombiex < playerx:
          movex = 1     # Move right
      elif zombiex > playerx:
          movex = -1    # Move left
      elif zombiex == playerx:
          movex = 0     # Don't move horizontally
          
      if zombiey < playery:
          movey = 1     # Move up
      elif zombiey > playery:
          movey = -1     # Move down
      elif zombiey == playery:
          movey = 0     # Don't move vertically
          
      # Check if zombie would run into a wall, and adjust
      
      if board[(zombiex + movex, zombiey + movey)] == WALL:
          # Zombie would run into a wall, so come up with new move
          if board[(zombiex + movex, zombiey)] == EMPTY_SPACE:
              movey = 0    # Zombie can't move horizontally
          elif board[(zombiex, zombiey + movey)] == EMPTY_SPACE:
              movex = 0    # Zombie can't move vertically
          else:
              # Zombie can't move
              movex = 0
              movey = 0
      newZombiex = zombiex + movex
      newZombiey = zombiey + movey
      
      if(board[(zombiex, zombiey)] == DEAD_ZOMBIE
          or board[(newZombiex, newZombiey)] == DEAD_ZOMBIE):
          # Zombie is at a crash site, remove it
          del zombiePositions[0]
          continue
          
      # Check if it moves into a zombie, then destroy both zombies
      if(newZombiex, newZombiey) in nextZombiePositions:
          board[(newZombiex, newZombiey)] = DEAD_ZOMBIE
          nextZombiePositions.remove((newZombiex, newZombiey))
      else:
          nextZombiePositions.append((newZombiex, newZombiey))
          
      # Remove zombies from zombiePositions as they move
      del zombiePositions[0]
  return nextZombiePositions
  
  
# If this program was run (instead of imported), run the game
if __name__ == '__main__':
    main()
