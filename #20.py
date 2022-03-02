'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''
# import modules

from random import sample

# define function that check for number in list


def check_num_in_list(list, num):
    return num in list


# generate list of 15 random numbers in range 200

list_of_numbers = [number for number in sample(range(200), 15)]


# get list in ascending order using sort()

list_of_numbers.sort()

# ask user for number and convert to int

num = int(input("Give me a number to check in list "))

# check if given number is in the list

num_in_list = check_num_in_list(list_of_numbers, num)

# print return boolean

print(num_in_list)
