number_n_one = int(input())
number_n_two = int(input())
operation = str(input())
even_or_odd = ''
if operation == '+':
    result = number_n_one + number_n_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_n_one} {operation} {number_n_two} = {result} - {even_or_odd}')
elif operation == '-':
    result = number_n_one - number_n_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_n_one} {operation} {number_n_two} = {result} - {even_or_odd}')
elif operation == '*':
    result = number_n_one * number_n_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_n_one} {operation} {number_n_two} = {result} - {even_or_odd}')
elif operation == '/':
    if number_n_two == 0:
        print(f'Cannot divide {number_n_one} by zero')
    else:
        result = number_n_one / number_n_two
        print(f'{number_n_one} / {number_n_two} = {result:.2f}')
elif operation == '%':
    if number_n_two == 0:
        print(f'Cannot divide {number_n_one} by zero')
    else:
        result = number_n_one % number_n_two
        print(f'{number_n_one} % {number_n_two} = {result}')
