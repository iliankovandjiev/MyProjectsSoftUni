import sys
n_numbers = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize
for _ in range (n_numbers):
    input_number = int(input())
    if input_number > max_number:
        max_number = input_number
    if input_number < min_number:
        min_number = input_number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
