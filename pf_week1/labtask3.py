# Task 3
number = input("Enter a number to check")
reverse_num = ""
for digit in number:
    reverse_num = digit + reverse_num

if number == reverse_num:
    print(number, "is a palindrome!")
else:
    print(number, "is not a palindrome,")

    