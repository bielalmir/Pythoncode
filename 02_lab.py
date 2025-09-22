num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))



addition = num1 + num2        
subtraction = num1 - num2     
multiplication = num1 * num2  

# Division (checking if denominator is not zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"


print("\nResults of Arithmetic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
