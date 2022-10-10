input_operation = input()
first_number = int(input())
second_number = int(input())


def solve(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


print(int(solve(first_number, second_number, input_operation)))