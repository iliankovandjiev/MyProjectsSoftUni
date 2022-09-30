import sys

numbers = input()
max_num = -sys.maxsize
while numbers != 'Stop':
    new_num = int(numbers)
    if new_num > max_num:
        max_num = new_num
    numbers = input()
print(max_num)
