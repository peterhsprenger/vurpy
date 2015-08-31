from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

#print_board(board)
print len(board)

def random_row(board):
    print randint(0, len(board))

def random_col(board):
    print randint(0, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)
board[int(ship_row)][int(ship_col)] = "X"
print_board(board)

'''
print "Reihe:", ship_row + 1, " | Spalte:", ship_col + 1


guess_row = (int(raw_input("Guess Row:"))) -1
print "Getippte Reihe:", guess_row
guess_col = (int(raw_input("Guess Col:"))) -1
print "Getippte Spalte:", guess_col

print "Reihe:", ship_row + 1
print "Spalte:", ship_col + 1

# Write your code below!
if guess_col == ship_col and guess_row == ship_col:
    print "Congratulations! You sank my battleship!"
elif guess_col not in range(5) or guess_row not in range(5):
    print "Oops, that's not even in the ocean."
elif board[(int(guess_row)) - 1][(int(guess_col)) - 1] == "X":
    print "You guessed that one already."
else:
    print "You missed my battleship!"
    board[[(int(guess_col))][(int(guess_row))]] = "X"
    print_board(board)
'''