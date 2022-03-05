'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
'''


def find_overlap_num(happy_num, prime_num):
    # using readlines make a list of numbers
    happy_num = happy_num_file.readlines()
    prime_num = prime_num_file.readlines()
    # iterate through one list and check if second list contains its elements, if yes strip and add to new list
    overlap_numbers = [num.strip('\n')
                       for num in happy_num if num in prime_num]
    return overlap_numbers


with open('happynumbers.txt') as happy_num_file, open('primenumbers.txt') as prime_num_file:  # open files for read

    # call function and print number that are overlapping
    print(find_overlap_num(happy_num_file, prime_num_file))
