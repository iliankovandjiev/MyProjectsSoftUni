number_of_cities = int(input())
day = 0
total_profit = 0
for city in range(number_of_cities):
    it_rainy_city = False
    day += 1
    name_of_city = input()
    money_owner_earns = float(input())
    owner_expenses = float(input())
    profit_for_each_city = 0

    if day % 3 == 0:
        owner_expenses *= 1.5
    if day % 5 == 0:
        money_owner_earns -= 0.1 * money_owner_earns
        if day % 3 == 0:
            it_rainy_city = True
    if not it_rainy_city:
        profit_for_each_city += money_owner_earns - owner_expenses
        total_profit += profit_for_each_city
    else:
        profit_for_each_city += money_owner_earns - owner_expenses / 1.5
        total_profit +=profit_for_each_city
    print(f'In {name_of_city} Burger Bus earned {profit_for_each_city:.2f} leva.')
print(f'Burger Bus total profit: {total_profit:.2f} leva.')