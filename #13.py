'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''


def get_amount_fib_num_to_generate():
    amountOfFibNum = int(
        input("How many fibonnaci numbers you want to generate? "))
    return amountOfFibNum


def get_list_of_fib_num(amountOfFibNum):

    if amountOfFibNum == 0:
        fibNumbers = []
    elif amountOfFibNum == 1:
        fibNumbers = [1]
    elif amountOfFibNum == 2:
        fibNumbers = [1, 2]
    elif amountOfFibNum > 2:
        fibNumbers = [1, 2]
        i = 0
        while i < (amountOfFibNum - 2):
            fibNumbers.append(fibNumbers[i] + fibNumbers[i + 1])
            i += 1
    return fibNumbers


amountOfFibNumbers = get_amount_fib_num_to_generate()

listOfFibNumbers = get_list_of_fib_num(amountOfFibNumbers)
