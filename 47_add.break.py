numbers = []
print("Enter numbers (enter -1 to stop):")

while True:
    num = int(input())
    if num <0:  
        break
    numbers.append(num)

print("You entered:", numbers)

length= len(numbers)
listSum= sum(numbers)
mean= listSum/length

print(mean)

