# Task 3
start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))

total_sum = 0

print("Prime numbers in this range:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
            total_sum = total_sum + num

print("The sum of these prime numbers is:", total_sum)