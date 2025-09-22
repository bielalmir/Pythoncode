# Program to iterate over a string

import time
from datetime import datetime

text = input("Enter a string: ")

print("Iterating over the string:")  #this loop will repeat every word in string one by one
for char in text:
    print(char)

    time.sleep(1)

print(datetime.today())