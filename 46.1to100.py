x = int (input("enter the values in the dictionary: "))
my_dict = {}

for i in range (x):
        key = input(f"enter key {i+1}: ")
        value = input(f"enter the value for {key}: ")
        my_dict[key] = value

print ("\niterate over dictionary: ")

print("\nkey: ")
for key in my_dict:
        print(key)

print ("\nvalue: ")
for value in my_dict.values():
        print(value)

print("\n key-values")
for key,value in my_dict.items():
        print(key, ":", value)

