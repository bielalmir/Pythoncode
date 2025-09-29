# num = int(input("enter a positive number :"))
# if num <=0:
#     print("not allowed :")
# elif num % 2 == 0:
#     print ("even :")
# elif num %2 !=0:
#     print("odd")
# else:
#     print("zero")



#Program to check if a number is prime

num = int(input("Enter a number: "))


if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("is not a prime number",num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")





# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0:
#         return False
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True

# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Please enter a valid integer.")
# else:
#     if is_prime(num):
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")
