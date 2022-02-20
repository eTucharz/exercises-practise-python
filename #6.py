'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

givenWord = input("Give some word").lower()

if givenWord == givenWord[::-1]:
    print("This is a palindrome!")

else:
    print("It's not a palindrome :(")
