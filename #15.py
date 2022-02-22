'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

# (1) using reverse()method

# create function that ask for string using input and return given string


def ask_for_string():
    givenString = input(
        "Please write some long string containing multiple words ")
    return givenString

# create function that takes given string as a parameter and return reversed string


def reverse_given_string(givenString):

    listOfWords = givenString.split()
    listOfWords.reverse()

    reversedString = ' '.join(listOfWords)
    return reversedString


givenString = ask_for_string()

reversedGivenString = reverse_given_string(givenString)

print(reversedGivenString)
