n_numbers = int(input())
total_sum1 = 0
total_sum2 = 0
abs_diff = 0
for i in range(n_numbers):
    input_number = int(input())
    if i % 2 == 0:
        total_sum1 += input_number
    else:
        total_sum2 += input_number
if total_sum1 == total_sum2:
    print('Yes')
    print(f'Sum = {total_sum1}')
else:
    abs_diff = abs(total_sum1 - total_sum2)
    print('No')
    print(f'Diff = {abs_diff}')
