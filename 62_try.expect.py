def divide_numbers(a, b):
    try:
        result = a / b   # risky operation
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Please enter only numbers.")
        result = None
    else:
        print("Division successful!")  # runs only if no exception occurs
    finally:
        print("Execution of divide_numbers function completed.")  # always runs
    return result


# Test cases
print("Result 1:", divide_numbers(10, 2))   # valid
print("Result 2:", divide_numbers(10, 0))   # zero division error
print("Result 3:", divide_numbers(10, "a")) # type error




#user input code

def safe_division():
    try:
        # Taking input from user
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))

        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid integers only.")
        result = None
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero.")
        result = None
    else:
        print("Division successful!")
    finally:
        print("Program execution completed.")
    
    return result


# Run the function
output = safe_division()
print("Result:", output)
