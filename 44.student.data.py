import numpy as np
import pandas as pd

print("=" * 50)

print(" Student Data Management System ")
print("=" * 50)

students_list = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    roll_no = int(input("Roll No: "))
    name = input("Name: ")
    age = int(input("Age: "))
    student_class = input("Class: ")
    marks = float(input("Marks: "))

    students_list.append([roll_no, name, age, student_class, marks])


df = pd.DataFrame(students_list, columns=["Roll No", "Name", "Age", "Class", "Marks"])

print("\n Student Records:")
print(df)

file_name = "student_records.csv"
df.to_csv(file_name, index=False)
print(f"\n Data saved successfully to '{file_name}'")


highest_scorer = df.loc[df["Marks"].astype(float).idxmax()]
print("\n Top Student:")
print(highest_scorer)