# Task 10
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Calculator")
print("1, Add")
print("2, Subtract")
print("3, Multiply")
print("4, Divide")

choice = int(input("Enter your choice"))
a = float(input("Enter first number"))
b = float(input("Enter second number"))

if choice == 1:
    print("Ans" , add(a, b))
elif choice == 2:
    print("Ans", subtract(a, b))
elif choice == 3:   
    print("Ans", multiply(a, b))
elif choice == 4:
    print("Ans", divide(a, b))
else:
    print("Invalid choice")