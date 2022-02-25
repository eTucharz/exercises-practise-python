from random import randint


def welcome_player():
    print("""Welcome in "Cows and Bulls"
Your main goal is to hit the 4 - digit number
If you hit some digit you will get the "COW"
Else you will get the "BULL"
When hit all digits the game it's over
Try to do that as fast as you can!""")


def get_number_from_player():
    givenNum = input("Give me 4 - digit number ")
    return givenNum


def generate_number():
    generatedNum = str(randint(1000, 9999))
    return generatedNum


def update_player_hits(givenNum, generatedNum):
    for i, v in enumerate(givenNum):

        if v == generatedNum[i]:
            playerGuesses["cow"] += 1
            i += 1
        else:
            playerGuesses["bull"] += 1
            i += 1
    return playerGuesses


def check_for_guess_number(playerGuesses):
    if playerGuesses["cow"] == 4:
        return True
    else:
        return False


def actualize_player_data(playerGuesses):
    playerGuesses["guesses"] += 1
    playerGuesses["cow"] = 0
    playerGuesses["bull"] = 0


def show_stats(playerGuesses):
    print(
        f'You have:\n{playerGuesses["cow"]} cows\n{playerGuesses["bull"]} bulls')


welcome_player()

playGame = True
generatedNum = generate_number()
playerGuesses = {"cow": 0, "bull": 0, "guesses": 0}

while playGame:

    givenNum = get_number_from_player()

    print(generatedNum)

    playerGuesses = update_player_hits(givenNum, generatedNum)

    isGuessNumber = check_for_guess_number(playerGuesses)

    if isGuessNumber:
        print(f'You guessed {playerGuesses["guesses"]} times before hit')
        playGame = False
    else:
        stats = show_stats(playerGuesses)
        actualize_player_data(playerGuesses)
