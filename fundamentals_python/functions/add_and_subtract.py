def sum_numbers(first, second):
    return first + second


def subtract(function, third):
    return function - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second, third)
    return result


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(add_and_subtract(number_one, number_two, number_three))
