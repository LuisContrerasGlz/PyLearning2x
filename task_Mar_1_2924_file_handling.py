# File Handling
# How to read a text, and write into it using python code

# Function, open("File_name", Mode)

# Mode

"""

r - reading (default)
w - for writing (creates a new file or truncates an existing one)
a - for appending
b - binary mode
+ - for updating (reading and writing)

"""

# Read and write content

"""

Read a file:

Reading Entire Content: content = file_object.read()
line = file_object.readline() for a single line
lines = file_object.readlines() for all lines in a list 

"""
# Close the file

file = open("TestData.txt", "r")
content = file.read()
print(content)
file.close

