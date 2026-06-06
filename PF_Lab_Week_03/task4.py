# Task 4
def f_to_c(f):
    c = (f-32) * 5/9
    return round(c, 2)

def c_to_f(c):
    f = (c * 9/5) + 32
    return round(f, 2)

fahrenheit = float(input("Enter temperature in fahrenheit:"))
print(fahrenheit, "F is equal to", f_to_c(fahrenheit), "C")

Celsius = float(input("Enter temperature in Celsius"))
print(Celsius, "C is equal to", c_to_f(Celsius), "F")