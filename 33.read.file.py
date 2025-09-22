file_name = "example.txt"
with open (file_name, "w") as file:
    file.write("hello world it's bilal\n")
    file.write("i am done on my studies\n")
    file.write("i am from jammu & Kashmir\n")

print("written in file sucessfully\n")
print("reading from file\n")

with open (file_name, "r")as file:
    content = file.read()
    print(content)