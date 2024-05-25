from math import *


# By Mohammad Janahi

def add(num1, num2):
    return num1 + num2


def subt(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return float(num1 / num2)


def exp(num1, num2):
    return num1 ** num2


print("Welcome to \"pycalc\" a python calculator")

while True:
    try:
        usertimes = int(input("How many math operations do you want to do? "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

for x in range(usertimes):
    print("""
Please Enter a number to apply the mathematical operation on two numbers:
Enter 1: To Apply Addition
Enter 2: To Apply Subtraction
Enter 3: To Apply Multiplication
Enter 4: To Apply Division
Enter 5: To Apply Exponentials
    """)

    while True:
        try:
            useropp = int(input("Enter your choice: "))
            if useropp not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid operation")
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if useropp == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif useropp == 2:
        print(num1, "-", num2, "=", subt(num1, num2))
    elif useropp == 3:
        print(num1, "x", num2, "=", mult(num1, num2))
    elif useropp == 4:
        result = div(num1, num2)
        if result == "Cannot divide by zero":
            print(result)
        else:
            print(num1, "/", num2, "=", result)
    elif useropp == 5:
        print(num1, "**", num2, "=", exp(num1, num2))

print("Thank you for using pycalc")