'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
'''

name = input("Hello, I'm Frank. What's your name? ")
print(f"Hi!{name}")
age = int(input("Please tell me how old are you? "))
presentYear = 2022
futureYear = (100 - age) + 2022
print(f"Nice! So, when you turn 100 we will have {futureYear}!")
number = int(input("Okay, now give me a random number "))
print(f"I'll show you this message {number} times \n" * number)
