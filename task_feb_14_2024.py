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

# Using for Loop

or_str = "Using a for loop now"
rev_or_srt = ""
for i in or_str:
    rev_or_srt =  i + rev_or_srt
print(rev_or_srt)

# Making it a function

def rev_str_for(or_str2):
    rev_or_srt2 = ""
    for i in or_str2:
        rev_or_srt2 =  i + rev_or_srt2
    return rev_or_srt2

print(rev_str_for("Using a for loop now"))

#Palindrome check

def check_palindrome(str_to_check):
    print(str_to_check.lower())
    print(rev_str_for(str_to_check).lower())
    if str_to_check.lower() == rev_str_for(str_to_check).lower():
        print("Palindrome :v ")
    else:
        print("not palindrome :v")

check_palindrome("LOL")

# --------------------------------------------------------------------------------------------------------------------------------------------

# Create a function to check if a string is palindrom 

def is_palindrome(input_string):
    # Remove spaces and convert the input string to lowercase
    input_string = input_string.replace(" ", "").lower()
    
    # Compare the input string with its reverse
    if input_string == input_string[::-1]:
        print("Palindrome")
        return True
    else:
        print("Not palindrome")
        return False


input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)

