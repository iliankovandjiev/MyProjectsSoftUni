budget_movie = float(input())
num_statist = int(input())
price_clothes = float(input())
decor_price = budget_movie * 0.1
if num_statist > 150:
    price_clothes = price_clothes * 0.9
total_price_clothes = price_clothes * num_statist + decor_price
if total_price_clothes > budget_movie:
    print('Not enough money!')
    print(f'Wingard needs {(total_price_clothes - budget_movie):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {(budget_movie - total_price_clothes):.2f} leva left.')