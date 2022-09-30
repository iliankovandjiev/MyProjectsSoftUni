n_numbers = int(input())
total_sum1 = 0
total_sum2 = 0
abs_diff = 0
for _ in range(n_numbers):
    input_number = int(input())
    total_sum1 += input_number
for _ in range(n_numbers):
    input_number = int(input())
    total_sum2 += input_number
if total_sum1 == total_sum2:
    print(f'Yes, sum = {total_sum1}')
else:
    abs_diff = abs(total_sum1 - total_sum2)
    print(f'No, diff = {abs_diff}')


