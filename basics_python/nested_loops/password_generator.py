numbers_total = int(input())
letters_total = int(input())
for digit_one in range(1, numbers_total + 1):
    for digit_two in range(1, numbers_total + 1):
        for letter_one in range(97, letters_total + 97):
            for letter_two in range(97, letters_total + 97):
                for digit_three in range (1, numbers_total + 1):
                    if digit_three > digit_one and digit_three > digit_two:
                        print(f'{digit_one}{digit_two}{chr(letter_one)}{chr(letter_two)}{digit_three}', end=' ')