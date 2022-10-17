def factorial(one, two):
    first_number = 1
    for num in range(2, one + 1):
        first_number *= num
    second_number = 1
    for num in range(2, two + 1):
        second_number *= num
    result = first_number / second_number
    return result


first_integer = int(input())
second_integer = int(input())
factorial_result = factorial(first_integer, second_integer)
print(f'{factorial_result:.2f}')
