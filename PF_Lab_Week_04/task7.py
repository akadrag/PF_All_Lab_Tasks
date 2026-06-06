# Task 7
# Task7
def maximum(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = maximum(55, 77, 34)
print("The largest number is", result)