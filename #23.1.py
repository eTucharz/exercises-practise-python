'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
'''


def get_list_of_num(file_to_read):
    with open(file_to_read) as f:
        return f.read().splitlines()


def get_list_of_overlap_numbers(list_1, list_2):
    overlap_numbers = [num for num in list_1 if num in list_2]
    return overlap_numbers


happy_numbers = get_list_of_num('happynumbers.txt')
prime_numbers = get_list_of_num('primenumbers.txt')

print(get_list_of_overlap_numbers(happy_numbers, prime_numbers))
