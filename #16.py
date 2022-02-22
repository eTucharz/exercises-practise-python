'''
Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project.
Feel free to skip this and come back when you’re more ready!

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

from random import sample, randrange, shuffle
import string

characters = string.printable
print(characters)

lengthOfPass = 20

number = randrange(lengthOfPass)
print(number)

numbersList = [number for number in range(10)]
randomNumbers = sample(numbersList, 5)
print(randomNumbers)

someList = ["a", "gp", "$*@"]

shuffle(someList)
print(someList)
