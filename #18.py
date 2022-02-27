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
    given_num = input("Give me 4 - digit number ")
    return given_num


def generate_number():
    generated_num = str(randint(1000, 9999))
    return generated_num


def check_player_hits(given_num, generated_num):
    player_hits = {"cow": 0, "bull": 0}
    for i, v in enumerate(given_num):
        if v == generated_num[i]:
            player_hits["cow"] += 1
        else:
            player_hits["bull"] += 1
        i += 1
    return player_hits


def check_for_guess_number(player_hits):
    if player_hits["cow"] == 4:
        return True
    else:
        return False


def show_player_hits(player_hits):
    return f'You have:\n{player_hits["cow"]} cows\n{player_hits["bull"]} bulls'


if __name__ == "__main__":

    welcome_player()

    play_game = True
    guesses = 0
    generated_num = generate_number()

    while play_game:

        given_num = get_number_from_player()

        print(generated_num)

        player_hits = check_player_hits(given_num, generated_num)

        is_guess_number = check_for_guess_number(player_hits)

        if is_guess_number:
            print(
                f'Congratulation! You guessed {guesses} times before hit')
            play_game = False
        else:
            stats = show_player_hits(player_hits)
            print(stats)
            guesses += 1
