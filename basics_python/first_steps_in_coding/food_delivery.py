chicken_menu = int(input())
fish_menu = int(input())
vegeta_menu = int(input())
price_menu = chicken_menu * 10.35 + fish_menu * 12.4 + vegeta_menu * 8.15
desert = price_menu * 0.2
delivery = 2.5
total_price = price_menu + desert + delivery
round_total_price = round(total_price, 2)
print(round_total_price)


