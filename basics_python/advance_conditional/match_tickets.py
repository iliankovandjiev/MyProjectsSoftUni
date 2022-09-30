budget = float(input())
category = str(input())
num_people = int(input())
total_money = budget
money_needed = 0
if num_people <= 4:
    total_money = total_money * 0.25
elif num_people <= 9:
    total_money = total_money * 0.4
elif num_people <= 24:
    total_money = total_money * 0.5
elif num_people <= 49:
    total_money = total_money * 0.6
else:
    total_money = total_money * 0.75
if category == 'VIP':
    money_needed = 499.99 * num_people
elif category == 'Normal':
    money_needed = 249.99 * num_people
if money_needed <= total_money:
    money_left = total_money - money_needed
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = abs(total_money - money_needed)
    print(f'Not enough money! You need {money_needed:.2f} leva.')
