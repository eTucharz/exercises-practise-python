'''
Make a two-player Rock-Paper-Scissors game.
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''
# import IntEnum from enum
from enum import IntEnum

# create menu
Menu_plays = IntEnum("Menu_plays", "Rock Scissors Paper")

# set flag
playGame = True

# create dict with players points
playersPoints = {"player1": 0, "player2": 0}

# create function that ask player for play


def ask_player_for_play():
    print("Enter the play of player")
    print("(1) for Rock")
    print("(2) for Scissors")
    print("(3) for Paper")

# create function that return player play


def get_player_play():
    playOfPlayer = int(input())
    return playOfPlayer

# create function that compare players plays


def compare_plays(playOfPlayer1, playOfPlayer2):
    if (playOfPlayer1 == Menu_plays.Rock and playOfPlayer2 == Menu_plays.Rock) or (playOfPlayer1 == Menu_plays.Scissors and playOfPlayer2 == Menu_plays.Scissors) or (playOfPlayer1 == Menu_plays.Paper and playOfPlayer2 == Menu_plays.Paper):
        return "Tie!"

    elif (playOfPlayer1 == Menu_plays.Paper and playOfPlayer2 == Menu_plays.Rock) or (playOfPlayer1 == Menu_plays.Rock and playOfPlayer2 == Menu_plays.Scissors) or (playOfPlayer1 == Menu_plays.Scissors and playOfPlayer2 == Menu_plays.Paper):
        playersPoints["player1"] += 1
        return "Player 1 win!"

    elif (playOfPlayer1 == Menu_plays.Scissors and playOfPlayer2 == Menu_plays.Rock) or (playOfPlayer1 == Menu_plays.Paper and playOfPlayer2 == Menu_plays.Scissors) or (playOfPlayer1 == Menu_plays.Rock and playOfPlayer2 == Menu_plays.Paper):
        playersPoints["player2"] += 1
        return "Player 2 win!"

# create function that show result


def show_result(result):
    print(result)

# create function that ask player for start new game


def ask_player_to_start_new_game():
    print("Do you want play again?")
    print('Type "y" for yes or "n" for no')
    wantPlayNewGame = input().lower()
    return wantPlayNewGame

# create function that show statistics


def show_statistics():
    for player, points in playersPoints.items():
        print(player)
        print(points)


while playGame:
    ask_player_for_play()

    playOfPlayer1 = get_player_play()
    playOfPlayer2 = get_player_play()

    result = compare_plays(playOfPlayer1, playOfPlayer2)
    show_result(result)

    wantPlayNewGame = ask_player_to_start_new_game()

    if wantPlayNewGame == "n":
        break
    else:
        show_statistics()
        continue
