#iterate over a list
import time
from datetime import datetime

items = input("Enter list elements separated by commas: "). split(".")

print("Iterating over the list:")
for item in items:
    print(item.strip())   # strip() removes extra spaces
    time.sleep(1)

print (datetime.today ())