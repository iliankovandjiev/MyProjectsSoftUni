number = int(input())
for row in range(1, number + 1):
    for columns in range(1, row + 1):
        print('$', end=' ')
    print()