# Task 4
import math

x1 = float(input("Enter x1"))
y1 = float(input("Enter y1"))
x2 = float(input("Enter x2"))
y2 = float(input("Enter y2"))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if x1 > 0 and y1 > 0:
    location = "1st Quadrant"
elif x1 < 0 and y1 > 0:
    location = "2nd Quadrant"
elif x1 < 0 and y1 < 0:
    location = "3rd Quadrant"
elif x1 > 0 and y1 < 0:
    location = "4th Quadrant"
else:
    location = "on the Axis or Origin"

print("The distance between points is", distance)
print("Point 1 is located in the", location)