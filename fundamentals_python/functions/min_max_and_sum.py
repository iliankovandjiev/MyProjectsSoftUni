sequence_of_numbers = input().split(' ')
sequence_of_numbers = [int(i) for i in sequence_of_numbers]
min_numbers = min(sequence_of_numbers)
max_numbers = max(sequence_of_numbers)
sum_of_all = sum(sequence_of_numbers)

print(f'The minimum number is {min_numbers}\n'
      f'The maximum number is {max_numbers}\n'
      f'The sum number is: {sum_of_all}' )