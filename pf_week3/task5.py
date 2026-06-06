# Task 5
def calculate_gpa():
    n = int(input("How many subjects did uou study?"))

    total_points = 0
    total_credits = 0

    for i in range(n):
        gp = float(input("Enter Grade Point:"))
        ch = int(input("Enter Credit hours:"))

        total_points = total_points + (gp * ch)
        total_credits = total_credits + ch

    result = total_points / total_credits
    return result

answer = calculate_gpa()
print("Your GPA is:", round(answer, 2))
