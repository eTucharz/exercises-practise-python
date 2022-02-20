'''
Take two lists and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
'''
from random import sample

# create 2 diffrent lists
list1 = [number for number in range(10)]
list2 = [number for number in range(5, 15)]

# print elements of above lists
print(list1)
print(list2)

# radomly generate 2 lists to test
for _ in range(2):
    randomlist1 = sample(range(10, 30), 5)
    randomlist2 = sample(range(10, 30), 5)

# create the function that return list of common elements  between list1 and list2


def get_duplicates(list1, list2):
    listOfDuplicates = [number for number in list1 if number in list2]
    return listOfDuplicates


# call a function
duplicates = get_duplicates(list1, list2)
print(duplicates)
