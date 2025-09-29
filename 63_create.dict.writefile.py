#problem = Write a program to create a directory, write a file in it, and handle any exceptions that occur.

import os

try:
    # Take user input for directory and file
    dir_name = input("Enter directory name: ")
    file_name = input("Enter file name (with extension): ")

    # Create directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    else:
        print(f"Directory '{dir_name}' already exists.")

    # Full path for the file
    file_path = os.path.join(dir_name, file_name)

    # Take content input from user
    content = input("Enter content to write in the file: ")

    # Write content to file
    with open(file_path, "w") as f:
        f.write(content)
    print(f"File '{file_name}' created successfully in '{dir_name}'.")

except PermissionError:
    print("Error: You don't have permission to create files here.")
except FileNotFoundError:
    print("Error: Directory path not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
