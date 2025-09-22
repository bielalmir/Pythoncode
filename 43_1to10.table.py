# Multiplication table from 1 to 10 using nested loop

for i in range(1, 11):      # Outer loop for numbers 1 to 10
    for j in range(1, 11):        # Inner loop for table of each number
        print(f"{i} x {j} = {i * j}", end='\t')
    print()                 # Newline after each table
