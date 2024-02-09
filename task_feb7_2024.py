# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of a circle: "))

area_of_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")
