budget = float(input())
season = input()
type_class = ''
type_car = ''
price = 0
if budget <= 100:
    type_class = 'Economy class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = 0.35 * budget
    elif season == 'Winter':
        type_car = 'Jeep'
        price = 0.65 * budget
elif budget <= 500:
    type_class = 'Compact class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = 0.45 * budget
    elif season == 'Winter':
        type_car = 'Jeep'
        price = 0.80 * budget
else:
    type_class = 'Luxury class'
    type_car = 'Jeep'
    price = 0.90 * budget
print(type_class)
print(f'{type_car} - {price:.2f}')




