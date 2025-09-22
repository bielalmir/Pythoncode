y = []
while True:
    store= input("Enter number or k to exit: ")
    if(store=='k'):
        break
    else:
        y.append(store)
length = len(y)
maximum = max(y)
minimum = min(y)

print("List:", y)

print("Length of the list:", length)

print("Maximum value in the list:", maximum)

print("Minimum value in the list:", minimum) 