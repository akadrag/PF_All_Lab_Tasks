# Task 2
for i in range(1, 5):
    for j in range(4-i):
        print(' ', end='\t')
    for i in range(2*i-1):
        print('*', end='\t')
    print()
for i in range(3, 0, -1):
    for j in range(4-i):
        print(' ', end='\t')
    for i in range(2*i-1):
        print('*', end='\t')
    print()