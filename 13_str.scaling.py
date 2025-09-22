# Program for string slicing

string = input("Enter a string: ")

start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

# Slicing
sliced = string[start:end]

print("Sliced String:", sliced)