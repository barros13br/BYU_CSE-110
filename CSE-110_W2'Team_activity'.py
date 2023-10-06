"""Write a program to compute the areas of three different shapes. Prompt for the necessary 
information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared."""

import math
 
 
#here is the math for square
length = float(input("Please, type the length of the square: "))
 
area_of_square = length ** 2
 
print (f"The area of the sqaure is {area_of_square:.1f}")
 
#here is the math for rectangle
rectlen = float(input("What is the length of the rectangle? "))
 
rectwid = float(input("What is the width of the rectangle? "))
 
area = rectlen * rectwid
 
print (f"The area of the rectangle is {area:.1f}")
 
#here is the area of the cirlce
radius = float(input("Please input the rads of the circle? " ))
 
#equasion
area_of_circle = math.pi  * radius *  radius
 
#Print of circle                                                                          
print (f"The area of the circle is {area_of_circle:.1f}")