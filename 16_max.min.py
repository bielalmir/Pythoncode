numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))
length = len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("List:", numbers)

print("Length of the list:", length)

print("Maximum value in the list:", maximum)

print("Minimum value in the list:", minimum) 