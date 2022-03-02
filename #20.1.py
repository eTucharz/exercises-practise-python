'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''

# import modules

from random import sample

# define function that find middle in list


def check_num_in_list(input_list, num):

    while len(input_list) > 0:
        middle = float(len(input_list)) / 2
        middle_num = input_list[int(middle - .5)]
        print(middle_num)
        if len(input_list) == 1:
            return num == middle_num

        elif num > middle_num:
            input_list = input_list[int(middle + .5):]
            print(input_list)

        elif num < middle_num:
            input_list = input_list[:int(middle - .5)]
            print(input_list)

    # else:
        # get middle num whe list even
        # middle_num = (input_list[int(middle)], input_list[int(middle - 1)])


# generate list of 15 random numbers in range 200
list_of_numbers = [number for number in sample(range(200), 15)]
# if middle % 2 != 0:
# num to check

num = 120

# get list in ascending order using sort()

list_of_numbers.sort()
print(list_of_numbers)


# check for num in list
result = check_num_in_list(list_of_numbers, num)
print(result)
