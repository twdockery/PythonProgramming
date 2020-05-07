##########################################################
# This will be to create a battleship game
# in a 5x5 grid. 10 guesses to win
##########################################################
from random import randint #this creates a random integer. For example: coin = randint(0,1) allows win or not. For another example: dice = randint(1,6) allows a random number from 1 to 6

board = [] # creates an empty list for the board
turn = 0   # sets initial turn to zero

for i in range(5): # creates a 5-row board
  board.append(["O"] * 5)

def print_board(board_in):
  for everyItem in board_in:
    print("  ".join(everyItem)) # .join replaces the " and ,

def random_row(board_in): # chooses a random row based on length
  return randint(1, len(board_in))

def random_col(board_in): # chooses a random column based on length
  return randint(1, len(board_in))



##########################################################
# This is the main game
##########################################################
print_board(board) #runs these functions
ship_row = random_row(board)
ship_col = random_col(board)

##########################################################
# debugging area
print(ship_row, ship_col)
##########################################################

##########################################################
# Guessing Loop
##########################################################
for turn in range(4):
  guess_row = int(input("Which Row: "))
  guess_col = int(input("Which Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif (board[guess_row][guess_col] == 'X'):
      print("You guessed that one already. Look at the board.")
    else:
      print("You missed my battleship!")
      board[guess_row - 1][guess_col - 1] = "X"
      turn += 1
      print("TURN: %s" % (turn))
      print_board(board)
  if turn == 10:
    print('GAME OVER ')
    break