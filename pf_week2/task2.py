# Task2
sentence = input("Enter a sentence")
sentence = sentence.lower()

vowels = 0
consonants = 0

for char in sentence:
    if 'a' <= char in "aeiou":
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)