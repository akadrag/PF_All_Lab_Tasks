# Task 5 
import math

a = float(input("Enter value for a"))
b = float(input("Enter value for b"))
c = float(input("Enter value for c"))

d = (b**2) - (4 * a * c)

if d == 0:
    print("Roots are real, equal and rational")
elif d > 0:
    print("Roots are real, distinct and irrational")
else:
    print("Roots are imaginary")

if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1", root1)
    print("Root 2", root2)