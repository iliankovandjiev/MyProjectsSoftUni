first, second, third = input().split('.')
first = int(first)
second = int(second)
third = int(third)
if third < 9:
    third += 1
else:
    third = 0
    second += 1
    if int(second) > 9:
        second = 0
        first += 1
print(f'{first}.{second}.{third}')
