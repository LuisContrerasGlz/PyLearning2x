"""

Create a program that determines whether a given year is a leap year.



A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.



Input = 2024

Output = Leap year

"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

input_year = int(input("Enter a year: "))

result = is_leap_year(input_year)
print(f"{input_year} is a {result}.")

"""

Write a program that classifies a triangle based on its side lengths.


Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

3 Input

side 1, side 2 and side 3

output - Eq, Iso, Scalene -

Eq. = side 1 == side 2 = side 3

"""

def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

side1 = float(input("Enter the length of side 1 of the triangle: "))
side2 = float(input("Enter the length of side 2 of the triangle: "))
side3 = float(input("Enter the length of side 3 of the triangle: "))

result = classify_triangle(side1, side2, side3)
print(f"The giventriangle is {result}. based on the sides")

