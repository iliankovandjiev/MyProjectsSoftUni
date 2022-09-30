import math

n_input = int(input())
if n_input <= 2:
    for row in range(n_input):
        for column in range(n_input):
            if n_input <= 2:
                if row == 0:
                    print('*', end='')
                else:
                    print('|', end='')
        print()

else:
    if n_input % 2 != 0:
        roof = math.ceil(n_input / 2)
        house = math.floor(n_input / 2)

        for row in range(roof):
            for columns in range(row, roof - 1):
                print('-', end='')
            for columns in range(row):
                print('*', end='')
            for columns in range(row + 1):
                print('*', end='')
            for columns in range(row, roof - 1):
                print('-', end='')
            print()

        for row in range(house):
            for columns in range(n_input):
                if columns == 0 or columns == n_input - 1:
                    print('|', end='')
                else:
                    print('*', end='')
            print()
    else:
        roof = int(n_input / 2)
        house = int(n_input / 2)

        for row in range(roof):
            for columns in range(row, roof - 1):
                print('-', end='')
            for columns in range(row + 1):
                print('*', end='')
            for columns in range(row + 1):
                print('*', end='')
            for columns in range(row, roof - 1):
                print('-', end='')
            print()

        for row in range(house):
            for columns in range(n_input):
                if columns == 0 or columns == n_input - 1:
                    print('|', end='')
                else:
                    print('*', end='')
            print()

