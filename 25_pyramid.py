#use nested loop to print a pyramid

rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    
    for space in range(rows - i): 
        print("", end="")

    
    for star in range(2 * i - 1): 
        print("*", end="")

    
    print() 
