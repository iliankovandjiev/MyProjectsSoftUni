number_input = int(input())
for row in range(number_input + 1):
    for column in range(row, number_input):
        print(' ', end='')

    for column in range(1, row + 1):
        print('*', end='')

    for column in range(1):
        print(' | ', end='')

    for column in range(1, row + 1):
        print('*', end='')

    print()