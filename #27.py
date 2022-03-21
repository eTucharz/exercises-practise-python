def get_co_ordinates_from_player():
    co_ordinates = input(
        'Please type co-ordinates\nFor example type "1,1" to move in first row in first column')
    co_ordinates = co_ordinates.split(",")
    co_ordinates = [int(i) - 1 for i in co_ordinates]
    return co_ordinates


def actualize_board(co_ordinates, player):

    if board[co_ordinates[0]][co_ordinates[1]] == 0:
        if player == 1:
            board[co_ordinates[0]][co_ordinates[1]] = 'X'
            return board
        elif player == 2:
            board[co_ordinates[0]][co_ordinates[1]] = 'O'
            return board

    elif board[co_ordinates[0]][co_ordinates[1]] == 'O' or 'X':
        return "You type co-ordinates that actually are occupied "


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]
         ]

play_game = True
players = [1, 2]

while play_game:
    for player in players:
        co_ordinates = get_co_ordinates_from_player()
        print(actualize_board(co_ordinates, player))
