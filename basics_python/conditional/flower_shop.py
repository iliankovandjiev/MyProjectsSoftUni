import math

magnolia = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
price_gift = float(input())
total_money = magnolia * 3.25 + hyacinths * 4 + roses * 3.5 + cactus * 8
money_after_tax = total_money * 0.95
abs_money = abs(money_after_tax - price_gift)
if money_after_tax >= price_gift:
    print(f'She is left with {math.floor(abs_money)} leva.')
else:
    print(f'She will have to borrow {math.ceil(abs_money)} leva.')


