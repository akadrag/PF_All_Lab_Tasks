# Task 2
ecat = float(input("Enter your ECAT marks:"))
inter = float(input("Enter your Intermediate marks:"))
matric = float(input("Enter your Matric marks:"))
ecat = (ecat / 400) * 33
inter = (inter / 1200) * 50
matric = (matric / 1100) * 17
Aggregate = ecat + inter + matric
print("Your total Aggregate is:", Aggregate)