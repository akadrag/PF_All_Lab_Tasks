# Task 3
upper = lambda text: text.upper()
def invert(text):
    reversed_text = text[::-1]
    print("Inverted string:", reversed_text)

user_input = input("Enter a string:")

uppercased = upper(user_input)
print("uppercased string:", uppercased)

invert(uppercased)