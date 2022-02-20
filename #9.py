'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint


def get_random_number():
    drawnNumber = randint(1, 9)
    return drawnNumber


def get_user_number():
    givenNumber = int(input("Guess drawn number. It's between 1 and 9. "))
    return givenNumber


def is_given_number_smaller_than_drawn_number(drawnNumber, givenNumber):
    if givenNumber < drawnNumber:
        return True
    else:
        return False


def is_given_number_higher_than_drawn_number(drawnNumber, givenNumber):
    if givenNumber > drawnNumber:
        return True
    else:
        return False


def ask_user_want_continue_game():
    print('Do you want continue guessing or start new game?\nType:\n"y" to keep guessing\n"n" to end game')
    wantContinueGame = input().lower()
    return wantContinueGame


def show_user_guesses_before_guessed():
    print(f"You guessed {playerGuesses} times before you guessed it")


playGame = True
playerGuesses = 0
drawnNumber = get_random_number()
print(drawnNumber)

while playGame:

    userNumber = get_user_number()
    isHigher = is_given_number_higher_than_drawn_number(
        drawnNumber, userNumber)

    if isHigher:
        playerGuesses += 1
        print("Given number is higher than drawn!")
    else:
        isSmaller = is_given_number_smaller_than_drawn_number(
            drawnNumber, userNumber)
        if isSmaller:
            playerGuesses += 1
            print("Given number is smaller than drawn!")
        else:
            print("You guessed!")
            show_user_guesses_before_guessed()
            break

    wantContinueGame = ask_user_want_continue_game()
    if wantContinueGame == "n":
        break
    else:
        continue
