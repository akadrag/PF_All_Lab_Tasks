# Task 1
import math

def calculate_npr(n, r):
    return math.factorial(n) // math.factorial(n-r)

def calculate_ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

n = int(input("Enter n: "))
r = int(input("enter r: "))

print("Permutation is ", calculate_npr(n, r))
print("Combination is ", calculate_ncr(n, r))