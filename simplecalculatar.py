print("                                    Simple Calculator\n")

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

print("You can choose one operator \n 1. +\n 2. -\n 3. *\n 4. /")

operator = input("Enter your operator: ")

if operator == "+":
    total = num1 + num2
    print("Total is", total)
elif operator == "-":
    total = num1 - num2
    print("Total is", total)
elif operator == "*":
    total = num1 * num2
    print("Total is", total)
elif operator == "/":
    if num2 == 0:
        print("Infinity (cannot divide by zero)")
    else:
        total = num1 / num2
        print("Total is", total)
else:
    print("Invalid operator")
