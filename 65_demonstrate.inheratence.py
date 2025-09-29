#pronnblem =   Write a program to demonstrate inheritance.


# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child Class inheriting Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        # Call parent constructor
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    
    def display(self):
        # Reuse parent method
        super().display()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")
course = input("Enter your course: ")

# Create Student object
s = Student(name, age, student_id, course)

# Display details
print("\n--- Student Details ---")
s.display()
