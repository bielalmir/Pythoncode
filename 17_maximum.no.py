numbers = input("enter a list :")
numbers = list(map(int, numbers.split()))

length = len(numbers)
minimum = min(numbers)

print("length of the list is :", numbers )
print("the minimum number is : ", minimum)
