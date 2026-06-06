# Task 2
ob_marks = int(input("Enter your marks:"))
total_marks = int(input("Enter total marks:"))
result = (ob_marks / total_marks) * 100
if result >= 90:
    print("A+")
elif result >= 85:
    print("A-")
elif result>= 80:
    print("B+")
elif result >= 75:
    print("B-")
elif result >= 70:
    print("C+")
elif result >= 65:
    print("C-")
elif result >= 60:
    print("F")