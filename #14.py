'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

listWithDuplicates = [1, 3, 7, 8, 10, 11, 10, 7, 1, 4, 4]

# get list of elements without duplicates using loop


def get_list_without_duplicates(list):
    listWithoutTDuplicates = []
    for element in list:
        if element not in listWithoutTDuplicates:
            listWithoutTDuplicates.append(element)
    return listWithoutTDuplicates


listWithoutDuplicates = get_list_without_duplicates(listWithDuplicates)
print(listWithoutDuplicates)

# get list of elements without duplicates using sets


def get_list_without_duplicates2(listWithDuplicates):
    listWithDuplicates = set(listWithDuplicates)
    listWithDuplicates = list(listWithDuplicates)
    return listWithoutDuplicates


listWithoutDuplicates2 = get_list_without_duplicates2(listWithDuplicates)
print(listWithoutDuplicates2)
