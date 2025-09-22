import time
from datetime import datetime

num = int(input("Enter a positive number: "))

i = 1

print(f"\nPrinting numbers from 1 to {num} using while loop:")

print (datetime.today())

while i <= num:
    print(i)
    i += 1    

    time.sleep(1)
