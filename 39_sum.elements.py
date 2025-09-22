# Function to calculate sum of list elements
def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

# Taking input from user
n = int(input("Enter number of elements in the list: "))
numbers = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)

# Calling the function
result = sum_of_list(numbers)

# Printing result
print("The sum of all elements in the list is:", result)
