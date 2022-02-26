'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number,
the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
'''


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


def check_player_hits(givenNum, generatedNum):
    for i, v in enumerate(givenNum):
        if v == generatedNum[i]:
            playerHits["cow"] += 1
        else:
            playerHits["bull"] += 1
        i += 1


def check_for_guess_number(playerHits):
    if playerHits["cow"] == 4:
        return True
    else:
        return False


def update_player_hits(playerGuesses):
    playerGuesses["guesses"] += 1
    playerGuesses["cow"] = 0
    playerGuesses["bull"] = 0


def show_player_hits(playerHits):
    return f'You have:\n{playerHits["cow"]} cows\n{playerHits["bull"]} bulls'


if __name__ == "__main__":

    welcome_player()

    playGame = True
    generatedNum = generate_number()
    playerHits = {"cow": 0, "bull": 0, "guesses": 0}

    while playGame:

        givenNum = get_number_from_player()

        print(generatedNum)

        check_player_hits(givenNum, generatedNum)

        isGuessNumber = check_for_guess_number(playerHits)

        if isGuessNumber:
            print(
                f'Congratulation! You guessed {playerHits["guesses"]} times before hit')
            playGame = False
        else:
            stats = show_player_hits(playerHits)
            print(stats)
            update_player_hits(playerHits)
