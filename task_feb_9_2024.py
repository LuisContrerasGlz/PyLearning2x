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
