#problem = Write a program to define a class and create objects.

# Define a class
class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")


# Take user input to create objects
n = int(input("Enter number of students: "))

students = []  # list to store student objects

for i in range(n):
    print(f"\nEnter details of student {i+1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll_no = input("Enter roll number: ")

    # Create object and add to list
    student = Student(name, age, roll_no)
    students.append(student)

# Display details of all students
print("\nStudent Details:")
for s in students:
    s.display_info()
