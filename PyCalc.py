from math import *
#By Mohammad Janahi
#https://github.com/Mhj63/Pycalc.git
def add(num1,num2):
    return num1+num2

def subt(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1* num2

def div(num1,num2):
    if num1 ==0 or num2 == 0:
        print ("0 can\'t be used in this opperation")
    return float(num1/num2)

def exp(num1,num2):
    return num1**num2

print("Welcome to \"pycalc\" a python calculator")
print("How many math operations do you want to do?")
usertimes=int(input())
for x in range(usertimes):
    print("""
Please Enter a number to apply the mathimatical operation on two numbers:
Enter 1: To Apply Addition
Enter 2: To Apply Subtraction
Enter 3: To Apply Multiplication
Enter 4: To Apply Division
Enter 5: To Apply Exponentials
    """)
    useropp=int(input())
    num1= int(input("Enter the first number:\n"))
    num2= int(input("Enter the second number:\n"))
    if useropp == 1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif useropp == 2:
        print(num1,"-",num2,"=",subt(num1,num2))
    elif useropp == 3:
        print(num1,"x",num2,"=",mult(num1,num2))
    elif useropp == 4:
        print(num1,"/",num2,"=",div(num1,num2))
    elif useropp == 5:
        print(num1,"**",num2,"=",exp(num1,num2))
    else:
        print(useropp,"is invalid enter a number that is between 1 and 5")
        break



print("Thank you for using pycalc")