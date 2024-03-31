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

# Same but using with keyword 

try:
    with open ("TestData.txt", "r") as file2:
        content2 = file2.read()
        print(content2)
except FileNotFoundError as fnfr:
    print(fnfr)

"""
when using the with statement in Python for file handling, you don't need to explicitly close the file. 
The with statement ensures that the file is automatically closed when the block of code inside it exits, even if an exception occurs within the block.

It's considered a best practice to use the with statement for file handling in Python because it simplifies code and helps prevent common errors related to file management, such as forgetting to close the file.

"""
