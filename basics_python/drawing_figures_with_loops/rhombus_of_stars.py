number = int(input())
for row in range(number):
    for columns in range(row, number - 1):
        print(' ', end='')
    for columns in range(row + 1):
        print('*', end=' ')
    print()
for row in range(number - 1, 0, -1):
    for columns in range(row, number):
        print(' ', end='')
    for columns in range(row, 0, -1):
        print('*', end=' ')
    print()


