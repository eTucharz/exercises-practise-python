'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

givenNumber = int(input("Write some number "))

listOfDivisorsGivenNumber = [number for number in range(
    1, givenNumber + 1) if givenNumber % number == 0]


print(listOfDivisorsGivenNumber)
