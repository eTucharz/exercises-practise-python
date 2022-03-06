'''
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

'''


def check_board(board):
    # iterate through all players
    for i in range(1, 3):
        # check for horizontal win
        if board[0] == [i, i, i] or board[1] == [i, i, i] or board[2] == [i, i, i]:
            return i
        # check for vertical win in first column
        elif board[0][0] == i and board[1][0] == i and board[2][0] == i:
            return i
        # check for vertical win in second column
        elif board[0][1] == i and board[1][1] == i and board[2][1] == i:
            return i
        # check for vertical win in third column
        elif board[0][2] == i and board[1][2] == i and board[2][2] == i:
            return i
        # check for diagonal win from top lef to bottom right
        elif board[0][0] == i and board[1][1] == i and board[2][2] == i:
            return i
        # check for diagonal win from top right bottom left
        elif board[0][2] == i and board[1][1] == i and board[2][0] == i:
            return i
    # if nobody win
    else:
        return


# board game
board = [[0, 0, 0],
         [0, 0, 0],
         [1, 1, 1]

         ]

print(check_board(board))
