# Task 4 
import random
import string

length = int(input("Enter the length of the password"))
all_characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    character = random.choice(all_characters)
    password = password + character

print("Your generated password is :", password)