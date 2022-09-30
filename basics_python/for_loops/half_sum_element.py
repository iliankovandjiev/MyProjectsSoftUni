import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for i in range(n):
    input_number = int(input())
    sum_numbers += input_number
    if input_number > max_num:
        max_num = input_number
sum_others = sum_numbers - max_num
if sum_others == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - sum_others)
    print('No')
    print(f'Diff = {diff}')
