'''
Ask the user for a number. Depending on whether the number is even or odd
print out an appropriate message to the user.

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check(call it num) and one number to divide by(check)
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

num = int(input("Give me random number "))

if num % 2 == 0:
    print("You give me even number!")
    if num % 4 == 0:
        print("Your number is also a multiple of 4!")

elif num % 2 != 0:
    print("You give me odd number!")

print("Now, please give me two numbers to divide: ")
num = int(input("(1) "))
check = int(input("(2) "))

if num % check == 0:
    print(f"{num} divides into {check} evenly!")
else:
    print(f"{num} not divides evenly into {check}!")
