# Task 2
find_large = lambda a, b: max(a, b)
def print_table(n):
    for i in range(3, 11):
        print(n, "x", i, "=", n * i)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

larger_num = find_large(num1, num2)
print("The largest number is:", larger_num)

print_table(larger_num)