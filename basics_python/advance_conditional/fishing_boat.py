budget_group = int(input())
season = str(input())
number_fisherman = int(input())
price_of_boat = 0
if season == 'Spring':
    price_of_boat = 3000
elif season == 'Summer' or season == 'Autumn':
    price_of_boat = 4200
elif season == 'Winter':
    price_of_boat = 2600
if number_fisherman <= 6:
    price_of_boat = price_of_boat * 0.9
elif number_fisherman <= 11:
    price_of_boat = price_of_boat * 0.85
else:
    price_of_boat = price_of_boat * 0.75
if number_fisherman % 2 == 0 and not season == 'Autumn':
    price_of_boat = price_of_boat * 0.95
if budget_group >= price_of_boat:
    money_left = budget_group - price_of_boat
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = price_of_boat - budget_group
    print(f"Not enough money! You need {money_needed:.2f} leva.")
