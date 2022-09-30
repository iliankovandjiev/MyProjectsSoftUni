import sys

numbers = input()
min_num = sys.maxsize
while numbers != 'Stop':
    new_num = int(numbers)
    if new_num < min_num:
        min_num = new_num
    numbers = input()
print(min_num)
