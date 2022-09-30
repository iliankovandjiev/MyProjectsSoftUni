limit_one = int(input())
limit_two = int(input())
limit_three = int(input())
second_digit_is_prime = True
for first_digit in range(1, limit_one + 1):
    if first_digit % 2 != 0:
        continue
    for second_digit in range(2, limit_two + 1):
        second_digit_is_prime = True
        for i in range(2, second_digit):
            if second_digit % i == 0:
                second_digit_is_prime = False
                break
        if second_digit_is_prime:
            for third_digit in range(1, limit_three + 1):
                if third_digit % 2 != 0:
                    continue
                print(f'{first_digit} {second_digit} {third_digit}')
        else:
            continue
