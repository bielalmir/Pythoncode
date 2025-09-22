import os
import json

STDS = {
    "STUDENTS": {
        "stud1": {"NAME": "BHULLA", "roll": 66, "address": "CHINKIPORA"},
        "stud2": {"NAME": "EGO HATAILA", "roll": 3, "address": "PAGLAPORA"}
    }
}

folder_path = "."

png_count = 0
jpg_count = 0

for file in os.listdir(folder_path):
    if file.lower().endswith(".png"):
        png_count += 1
    elif file.lower().endswith((".jpg", ".jpeg")):
        jpg_count += 1

STDS["file_counts"] = {
    "png_files": png_count,
    "jpg_files": jpg_count
}

with open("test.json", "w") as output_file:
    json.dump(STDS, output_file, indent=4)

print("Data saved to test.json")
print(STDS)
