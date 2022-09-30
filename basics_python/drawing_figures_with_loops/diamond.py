import math

input_number = int(input())
if input_number % 2 != 0:
    input_number = math.ceil(input_number / 2)
    for row in range(input_number):
        for column in range(row, input_number - 1):
            print('-', end='')
        for column in range(row):
            if column == 0:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row + 1):
            if column == (row):
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row, input_number - 1):
            print('-', end='')
        print()

    for row in range(input_number - 1):
        for column in range(row + 1):
            print('-', end='')
        for column in range(row, input_number - 1):
            if column == row or column == input_number + 1:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row, input_number - 1):
            if column == input_number - 3:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row):
            print('-', end='')
        print()
else:

    input_number = int(input_number / 2)
    for row in range(input_number):
        for column in range(row, input_number - 1):
            print('-', end='')
        for column in range(row + 1):
            if column == 0:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row + 1):
            if column == row:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row, input_number - 1):
            print('-', end='')
        print()

    for row in range(input_number - 1):
        for column in range(row + 1):
            print('-', end='')
        for column in range(row, input_number - 1):
            if column == row or column == input_number + 1:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row, input_number - 1):
            if column == input_number - 2:
                print('*', end='')
            else:
                print('-', end='')
        for column in range(row + 1):
            print('-', end='')
        print()