'''
Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.
Randomly generate two lists to test this
'''

from random import sample

list1 = [number for number in sample(range(20), 10)]
list2 = [number for number in sample(range(17), 7)]
print(list1)
print(list2)
listWithCommonNumber = [number for number in list1 if number in list2]
print(listWithCommonNumber)
