first_number = int(input())
second_number = int(input())
for number_current in range(first_number, second_number + 1):
    number_to_str = str(number_current)
    odd_digit = 0
    even_digit = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_digit += int(digit)
        else:
            even_digit += int(digit)
    if odd_digit == even_digit:
        print(number_current, end=" ")








