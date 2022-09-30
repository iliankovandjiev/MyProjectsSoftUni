price_excursion = float(input())
puzzel_num = int(input())
dols_num = int(input())
bears_num = int(input())
minions_num = int(input())
truks_num = int(input())
price_puzzel = puzzel_num * 2.6
price_dols = dols_num * 3
price_bears = bears_num * 4.1
price_minions = minions_num * 8.2
price_truks = truks_num * 2
num_of_order = puzzel_num + dols_num +  bears_num + minions_num + truks_num
total_income = price_truks + price_minions + price_bears + price_dols + price_puzzel
if num_of_order >= 50:
    total_income = total_income * 0.75
money_left = total_income * 0.9
if money_left >= price_excursion:
    print(f'Yes! {(money_left - price_excursion):.2f} lv left.')
else:
    print(f'Not enough money! {(price_excursion-money_left):.2f} lv needed.')