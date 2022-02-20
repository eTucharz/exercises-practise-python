'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
'''

givenNumber = int(input("Give me a number!"))


def check_is_prime_number(givenNumber):

    if givenNumber > 1:

        for number in range(2, givenNumber):

            if (givenNumber % number) == 0:
                return(f"{givenNumber} is not a prime number")

            else:
                return(f"{givenNumber} is a prime number")

    else:
        return(f"{givenNumber} is not a prime number")


checkedNumber = check_is_prime_number(givenNumber)
print(checkedNumber)
