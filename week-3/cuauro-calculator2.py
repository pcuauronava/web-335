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

# variable creation
# first you show the user the required variable assignation
print("Please enter first number: ")
# the input is assigned to the variable "num1"
num1 = input()
print("Please enter second number: ")
# the input is assigned to the variable "num2"
num2 = input()
# show the offered operations
print("-------------------------")
print("Please select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("-------------------------")
# assign the selection to the variable "operation"
operation = input()
# condition the operation to the previously showed values
# the input is defined as a string
if operation == "1":
    # this part of code takes que string in stored in the variable num1 and converts it to a number
    # performs the arithmetic operation and then is converted again to string to be printed back to
    # the user
    print(num1 + " + "+num2+" is " + str(int(num1) + int(num2))+".")
elif operation == "2":
    print(num1 + " - "+num2+" is " + str(int(num1) - int(num2))+".")
elif operation == "3":
    print(num1 + " * "+num2+" is " + str(int(num1) * int(num2))+".")
elif operation == "4":
    print(num1 + " / "+num2+" is " + str(int(num1) / int(num2))+".")
else:
    # if the selection is different than the offered
    print("Invalid selection, please try again")
