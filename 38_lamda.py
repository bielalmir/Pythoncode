# Program to demonstrate lambda functions with user input

# Lambda to add two numbers
add = lambda x, y: x + y
print("enter number to add")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Addition:", add(x, y))

# Lambda to square a number
square = lambda n: n ** 2
n = int(input("Enter a number to find its square: "))
print("Square:", square(n))

# Lambda to check even or odd
is_even = lambda n: "Even" if n % 2 == 0 else "Odd"
num = int(input("Enter a number to check even/odd: "))
print("The number is:", is_even(num))

# Using lambda with map() - square all numbers entered by user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
squared_numbers = list(map(lambda n: n ** 2, numbers))
print("Squared list:", squared_numbers)

# Using lambda with filter() - filter even numbers from user input
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)
