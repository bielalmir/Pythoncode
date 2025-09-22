numbers = input ("enter a list :")
numbers = list(map(int, numbers.split()))

length = len(numbers)
maximum = max(numbers)

print ("the length of list is :", length)
print ("the maximum number is :", maximum)