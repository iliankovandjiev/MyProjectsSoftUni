numbers_input = input().split(' ')
abs_numbers = []
for num in numbers_input:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)