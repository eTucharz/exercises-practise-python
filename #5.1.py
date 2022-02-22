'''
Go back and do Exercise 5 using sets, and write the solution for that in a different function.

Take two sets and write a program that returns a list that contains only the elements that are common between the sets
(without duplicates).
Make sure your program works on two sets of different sizes.

Extras:

Randomly generate two sets to test this

'''
# import sample from random

from random import sample

# create function that checks common elements in set A and set B using conjunction. Next transform set into a list and return


def get_list_without_duplicates(A, B):
    C = A & B
    return list(C)

# create set A and set B with common elements


A = {number for number in range(10)}
B = {number for number in range(4, 15, 2)}

# create set E and F radomly to test

E = {number for number in sample(range(10, 30), 10)}
F = {number for number in sample(range(10, 30), 10)}

# call the function and printing list without duplicates
list_without_duplicates = get_list_without_duplicates(E, F)
print(list_without_duplicates)
