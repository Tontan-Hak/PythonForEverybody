# This program computes the area of a circle. It receives the radius as an input from the user.

# Import the math library so that we can use constant pi.
import math
# Get the radius 
radius = float(input("Enter the radius: "))

# Compute the area
area = math.pi * radius**2

# Display the area
print("The circle area of the circle is", round(area,2))