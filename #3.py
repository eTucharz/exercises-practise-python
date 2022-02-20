'''
Take a list and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list, that are smaller than that number given by the user.
'''
# This is the list of numbers from 0 to 9
listOfNumbers = [number for number in range(10)]
print(listOfNumbers)

# Printed elements of the list that are less than 5

for number in listOfNumbers:
    if number < 5:
        print(number)

# This is the list transformated from the above list with numbers less than 5

listOfNumbersAfterTransform1 = [
    number for number in listOfNumbers if number < 5]
print(listOfNumbersAfterTransform1)

# Return the list of elements that are smaller than number given by the user

givenNumber = int(input(
    f"Give a number not greater than {len(listOfNumbers) - 1} "))


def getListOfNumbers():
    if givenNumber in listOfNumbers:
        listOfNumbersAfterTransform2 = [
            number for number in range(givenNumber)]
        return listOfNumbersAfterTransform2


listOfNumbersAfterTransform2 = getListOfNumbers()
print(listOfNumbersAfterTransform2)
