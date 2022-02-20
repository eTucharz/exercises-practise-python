'''
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''
a = [5, 10, 15, 20, 25]


def get_list_of_extreme_numbers(givenList):
    listOfExtremeNumbers = [
        number for number in givenList if number == givenList[0] or number == givenList[-1]]
    return listOfExtremeNumbers


listOfExtremeNumbers = get_list_of_extreme_numbers(a)
print(listOfExtremeNumbers)
