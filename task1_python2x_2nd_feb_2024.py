# Task #1 - Take a user input (name, age, roll_number, phone_number) and print the user details.

user_name = input("please enter your name: ")
user_age = input("please enter your age: ")
user_roll_number = input("please enter your roll_number: ")
user_phone_number = input("please enter your phone_number: ")

print(f'Hello. {user_name}, to confirm your data, your age is {user_age}, your roll numer is {user_roll_number}, and your phone number is {user_phone_number}')

# Task #2 - Print the Table of 2 by using the command print()

print("Here is the table of 2: ")
for i in range(1, 11):
    table_2 = 2 * i
    print(f'2 x {i} = {table_2}')


