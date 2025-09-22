
with open('example.txt', 'r') as file:
    lines = file.readlines()


del lines[2]  


with open('file.txt', 'w') as file:
    file.writelines(lines)