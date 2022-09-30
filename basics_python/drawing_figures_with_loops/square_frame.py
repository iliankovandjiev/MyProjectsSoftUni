numbers = int(input())
for i in range(numbers):
    for y in range(numbers):
        if (i == 0 and y == 0) or (i == (numbers - 1) and y == (numbers - 1)) or (i == (numbers - 1) and y == 0) or (i == 0 and y == (numbers - 1)):
            simbol = '+'
            print(simbol, end=' ')
        elif y == 0 or y == (numbers - 1):
            simbol = '|'
            print(simbol, end=' ')
        else:
            simbol = '-'
            print(simbol, end=' ')
    print()