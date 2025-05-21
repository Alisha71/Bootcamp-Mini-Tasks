# Get the lengths of the triangle sides from users
import math


side1 = float(input("Enter the length of side 1:"))
side2 = float(input("Enter the lenth of side 2:"))
side3 = float(input("Enter the length of side 3:"))

# Calculate the half-perimeter (h) 
s = (side1 + side2 + side3) / 2

# Use formula to calculate the area
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3)) 

# Output of area 
print(f"The area of the triangle: {area}")

