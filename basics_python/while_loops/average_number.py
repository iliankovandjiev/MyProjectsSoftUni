number = int(input())
sum_number = 0
counter = 0
for i in range(number):
    number = int(input())
    sum_number += number
    counter += 1
div_sum = sum_number / counter
print(f'{div_sum:.2f}')