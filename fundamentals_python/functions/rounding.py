numbers_input = input().split(' ')
rounded_numbers = []
for num in numbers_input:
    rounded_numbers.append(round(float(num)))
print(rounded_numbers)