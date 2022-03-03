'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''

# import modules

from random import sample

# define function that check for num in list


def check_num_in_list(input_list, num):

    input_list.sort()  # sort list
    while len(input_list) > 0:

        # get index of middle number from list
        middle = float(len(input_list)) / 2

        # get middle number from list
        middle_num = input_list[int(middle - .5)]

        # check for number in list
        if middle_num == num:
            return num == middle_num  # return TRUE when number in list

        elif num > middle_num:
            # slice list to take numbers from middle to end
            input_list = input_list[int(middle + .5):]

        elif num < middle_num:
            # slice list to take numbers from start to middle
            input_list = input_list[:int(middle - .5)]

    return middle_num == num  # return FALSE when number not in list


if __name__ == "__main__":

    # generate list of 20 random numbers in range 200
    list_of_numbers = [number for number in sample(range(200), 20)]

    # number to check
    num = 40

    # call the function
    result = check_num_in_list(list_of_numbers, num)

    # print result
    print(result)
