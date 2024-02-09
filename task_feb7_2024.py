# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of a circle: "))

area_of_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

# Develop a Python script that calculates the square and cube of a given number.

def calculate_square(number):
    square = number ** 2
    return square

def calculate_cube(num):
    cube = num ** 3
    return cube

number = float(input("Enter a number: "))
num = float(input("Enter another number please(it could be the same): "))

square_result = calculate_square(number)
cube_result = calculate_cube(num)

print(f"The square of {number} is: {square_result}")
print(f"The cube of {num} is: {cube_result}")
