'''
Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project.
Feel free to skip this and come back when you’re more ready!

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be.
'''
# import modules

from random import sample, shuffle
from string import ascii_letters, digits, punctuation

# ask user if want generate password of standard length or custom


def ask_user_for_type_of_pass():
    print("Hey! Welcome in PassGen!\nNow you can generate your new password which be a mix of lowercase letters, uppercase letters, numbers, and symbols\nDefault password has 10 characters\nIf you want now generate password of standard length just click (y)\nOtherwise click (n)")
    wantGeneratePassOfStandardLength = input()
    return wantGeneratePassOfStandardLength

# define a function that ask user for number od characters to generate new password


def get_number_of_characters_for_generate_pass(wantGeneratePassOfStandardLength):
    numberOfCharactersForGeneratePass = 10
    if wantGeneratePassOfStandardLength == "y":
        return numberOfCharactersForGeneratePass
    else:
        numberOfCharactersForGeneratePass = int(
            input("Feel free to give amount of characters for yor new password"))
        return numberOfCharactersForGeneratePass

# define a function that generate pass of given length of characters


def generate_pass(numberOfCharactersForGeneratePass):
    characters = list(ascii_letters + digits + punctuation)
    shuffle(characters)
    generatedPass = "".join(
        sample(characters, numberOfCharactersForGeneratePass))
    return generatedPass

# define a function that print generated pass


def print_generated_pass(generatedPass):
    print(f"Your password: {generatedPass}")


wantGeneratePassOfStandardLength = ask_user_for_type_of_pass()

numberOfCharactersForGeneratePass = get_number_of_characters_for_generate_pass(
    wantGeneratePassOfStandardLength)

generatedPass = generate_pass(numberOfCharactersForGeneratePass)

print_generated_pass(generatedPass)
