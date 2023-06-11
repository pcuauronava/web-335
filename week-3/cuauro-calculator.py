# ==========================
# Title: cuauro_calculator.py
# Author: Richard Krasso
# Modified by: Patrick Cuauro
# Date: 8 Jun 2023
# Description: Exercise 3.3
# simple calculator
# ==========================
# functions
# add
# subtract
# divide
# multiply
# declare functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


# declaring the variables
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
choice = input(
    """
-------------------------
Select Function: 
1. Add
2. Subtract
3. Multiply
4. Divide                
-------------------------
""")
# condition the operation to the previously showed values
if choice == "1":
    total = add(num1, num2)
    print(num1, "+", num2, "is", total, ".")
elif choice == "2":
    total = subtract(num1, num2)
    print(num1, "-", num2, "is", total, ".")
elif choice == "3":
    total = multiply(num1, num2)
    print(num1, "*", num2, "is", total, ".")
elif choice == "4" and num1 == 0 or num2 == 0:
    # if one of the numbers is 0 return undefined
    print("Undefined.")
elif choice == "4":
    total = divide(num1, num2)
    print(num1, "/", num2, "is", total, ".")
else:
    # if the selection is different than the offered
    print("Invalid selection, please try again.")
