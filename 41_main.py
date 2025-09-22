# main.py
# Program that imports and uses custom module

import mymodule   # Importing the custom module

# Taking user input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", mymodule.add(x, y))
print("Subtraction:", mymodule.subtract(x, y))
print("Multiplication:", mymodule.multiply(x, y))
print("Division:", mymodule.divide(x, y))
