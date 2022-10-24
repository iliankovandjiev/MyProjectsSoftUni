list_of_numbers = input().split(', ')
int_of_numbers = list(map(int, list_of_numbers))
positive_numbers = [num for num in int_of_numbers if num >= 0]
negative_numbers = [num for num in int_of_numbers if num < 0]
even_numbers = [num for num in int_of_numbers if num % 2 == 0]
odd_numbers = [num for num in int_of_numbers if num % 2 != 0]
print(f'Positive: {", ".join([str(num) for num in positive_numbers])}')
print(f'Negative: {", ".join([str(num) for num in negative_numbers])}')
print(f'Even: {", ".join([str(num) for num in even_numbers])}')
print(f'Odd: {", ".join([str(num) for num in odd_numbers])}')


