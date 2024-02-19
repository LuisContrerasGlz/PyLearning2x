# Reverse a string

# Slicing method
 
string_to_reverse = "Hey this is the string to reverse!"
reversed_string = string_to_reverse[::-1]
print(reversed_string)

# reversed() + join()

# Reverse a string using reversed() and join()
original_string = "Hello, World!"
reversed_string2 = ''.join(reversed(original_string))
print(reversed_string2)

