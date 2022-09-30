coin_one = int(input())
coin_two = int(input())
banknote_five = int(input())
total_sum = int(input())
for one_lv in range(coin_one + 1):
    for two_lv in range(coin_two + 1):
        for five_lv in range(banknote_five + 1):
            total_cash = one_lv * 1 + two_lv * 2 + five_lv * 5
            if total_cash == total_sum:
                print(f'{one_lv} * 1 lv. + {two_lv} * 2 lv. + {five_lv} * 5 lv. = {total_sum} lv.')