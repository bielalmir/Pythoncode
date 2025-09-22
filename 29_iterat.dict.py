#program to iterate over dictionary
import pandas as pd
x = int(input("ente the values of the dictionary: "))
my_dict = {}

for i in range (x):
        item = input(f"enter a item {i + 1}: ")
        price = input(f"enter a price for {item}:")
        my_dict [item] = price

print("iterate over dictionary\n")

print("item")
for item in my_dict:
    print(item)


print ("\nprice")
for price in my_dict.values():
    print(price)

print("\nitem & price")

print(pd.DataFrame(list(my_dict.items())))
print("\n")
for item, price in my_dict.items():
     print(item,":",price)