
values = input("Enter multiple values separated by space: ")

values_list = values.split()

print("\nYou entered:")
for i, values in enumerate(values_list, start=1):
    print(f"Value {i}: {values}")
 