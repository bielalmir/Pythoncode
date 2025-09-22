
# In Python, you can read and write to files using different modes like:

# "r" → read (default, file must exist)

# "w" → write (creates/overwrites a file)

# "a" → append (adds to the file)

# "r+" → read and write (file must exist)

# "w+" → write and read (overwrites or creates file)

# "a+" → append and read (adds new data but allows reading too)

# Here’s a full program demonstrating each mode:



# Explanation:

# "w" → overwrites/creates a new file.

# "r" → reads file (must exist).

# "a" → appends text to the file.

# "r+" → reads and writes but doesn’t overwrite.

# "w+" → overwrites and allows reading.

# "a+" → appends and allows reading.


file_name = "sample.txt"

# -----------------------------
# Write mode: creates/overwrites the file
with open(file_name, "w") as f:
    f.write("This is written in write mode.\n")
    f.write("Previous content (if any) is deleted.\n")

# -----------------------------
# Read mode: read the content
with open(file_name, "r") as f:
    print("Reading in 'r' mode:")
    print(f.read())

# -----------------------------
# Append mode: add more content
with open(file_name, "a") as f:
    f.write("This line is appended.\n")

# -----------------------------
# Read + Write mode: 'r+' (file must exist)
with open(file_name, "r+") as f:
    content = f.read()
    print("\nReading in 'r+' mode:")
    print(content)
    f.write("Added using r+ mode.\n")

# -----------------------------
# Write + Read mode: 'w+' (overwrite)
with open(file_name, "w+") as f:
    f.write("This will overwrite the file.\n")
    f.seek(0)  # move cursor to beginning
    print("\nReading in 'w+' mode after writing:")
    print(f.read())

# -----------------------------
# Append + Read mode: 'a+' (append if exists)
with open(file_name, "a+") as f:
    f.write("Adding line in a+ mode.\n")
    f.seek(0)  # move cursor to start for reading
    print("\nReading in 'a+' mode:")
    print(f.read())
