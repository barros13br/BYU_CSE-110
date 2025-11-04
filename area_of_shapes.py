#prompt length of one square side 
square_side_lenght = float(input("What is the lenght of a side of the square? "))
print()
#doing the math
square_area = square_side_lenght * square_side_lenght
print(f"The area of the square is: {square_area:.2f}")
print("------------------------------------------------------------------")
#prompt retangle length and width
rectangle_lenght = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
print()
#doing math
rectangle_area = rectangle_lenght * rectangle_width
print(f"The area of the rectangle is: {rectangle_area:.2f}")
print("------------------------------------------------------------------")
#prompt circle radius
circle_radius = float(input("What is the radius of the circle? "))
print()
#doing the math
import math
circle_area = math.pi * (circle_radius * circle_radius)
print(f"The area of the circle is: {circle_area}")