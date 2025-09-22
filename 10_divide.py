while True:
    try:
     num1 = float(input("Enter the first number: "))
     num2 = float(input("Enter the second number: "))
     print(num1/num2)
    

    
    except ZeroDivisionError:
        print("Invaild input")
        continue
    else:
       break
        
