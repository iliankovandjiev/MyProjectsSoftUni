import math

input_number = int(input())
round_number = ''
for row in range(input_number):
    for column in range(input_number):
        if row == 0 or row == input_number - 1:
            print(2 * '*', end='')
        elif column == 0:
            print('*/', end='')
        elif column == input_number - 1:
            print('/*', end='')
        else:
            print(2 * '/', end='')


    for column in range(input_number):
        round_number = math.ceil(((input_number) / 2))
        if row == round_number - 1:
            print('|', end='')
        else:
            print(' ', end='')


    for column in range(input_number):
        if row == 0 or row == input_number - 1:
            print(2 * '*', end='')
        elif column == 0:
            print('*/', end='')
        elif column == input_number - 1:
            print('/*', end='')
        else:
            print(2 * '/', end='')
    print()