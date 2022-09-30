first_number = int(input())
second_number = int(input())
third_number = int(input())
its_true = False
for pin_one in range(1, first_number + 1):
    for pin_two in range(2, second_number + 1):
        for pin_three in range(1, third_number + 1):
            if pin_one % 2 == 0 and pin_three % 2 == 0 and (pin_two == 2 or pin_two == 3 or pin_two == 5 or pin_two == 7):
                its_true = True
                print(f'{pin_one} {pin_two} {pin_three}')

