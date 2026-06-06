# Task 5
stars = 5
for i in range(stars):
    for space in range(stars - i - 1):
        print(' ', end= '')
    for star in range(2*i + 1):
        print('*', end= '')
    print()
    