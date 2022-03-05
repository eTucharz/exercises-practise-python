'''
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics!
Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by
'''


def create_board(board_size):

    return (((((" ---" * int(board_size)) + " \n") + (("|   " * int(board_size)) + "|\n")))
            * int(board_size)) + (" ---" * int(board_size))


board_size = int(input(
    'Type board size. For example if you type "3", you create 3 x 3 board'))

print(create_board(board_size))
