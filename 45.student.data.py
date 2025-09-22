# Simple program to store and display student data

students = []  # list to store student details

# Number of students
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    roll_no = input("Roll Number: ")
    age = int(input("Age: "))
    student_class = input("Class: ")
    marks = float(input("Marks: "))
    
    # store details in a dictionary
    student = {
        "Roll No": roll_no,
        "Age": age,
        "Class": student_class,
        "Marks": marks
    }
    
    students.append(student)  # add to list

# Display all students
print("\n--- Student Data  ---")
for s in students:
    print(f"Roll No: {s['Roll No']}, Age: {s['Age']}, Class: {s['Class']}, Marks: {s['Marks']}")
