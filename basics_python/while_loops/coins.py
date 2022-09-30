change_cash = float(input())
lv_two = 0
lv_one = 0
coin_50 = 0
coin_20 = 0
coin_10 = 0
coin_5 = 0
coin_2 = 0
coin_1 = 0
while change_cash >= 0.01:
    while change_cash >= 0.02:
        while change_cash >= 0.05:
            while change_cash >= 0.10:
                while change_cash >= 0.20:
                    while change_cash >= 0.50:
                        while change_cash >= 1:
                            while change_cash >= 2:
                                lv_two = change_cash // 2
                                change_cash -= lv_two * 2
                                change_cash = round(change_cash, 2)
                                break
                            lv_one = change_cash // 1
                            change_cash -= lv_one * 1
                            change_cash = round(change_cash, 2)
                            break
                        coin_50 = change_cash // 0.5
                        change_cash -= coin_50 * 0.5
                        change_cash = round(change_cash, 2)
                        break
                    coin_20 = change_cash // 0.2
                    change_cash -= coin_20 * 0.2
                    change_cash = round(change_cash, 2)
                    break
                coin_10 = change_cash // 0.1
                change_cash -= coin_10 * 0.1
                change_cash = round(change_cash, 2)
                break
            coin_5 = change_cash // 0.05
            change_cash -= coin_5 * 0.05
            change_cash = round(change_cash, 2)
            break
        coin_2 = change_cash // 0.02
        change_cash -= coin_2 * 0.02
        change_cash = round(change_cash, 2)
        break
    coin_1 = change_cash // 0.01
    change_cash -= coin_1 * 0.01
    change_cash = round(change_cash, 2)
    break
total_coin = lv_two + lv_one + coin_50 + coin_20 + coin_10 + coin_5 + coin_2 + coin_1
print(f'{total_coin:.0f}')
