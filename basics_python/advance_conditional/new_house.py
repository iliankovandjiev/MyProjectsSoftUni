type_of_flowers = str(input())
number_of_flowers = int(input())
budget = int(input())
total_price = 0
if type_of_flowers == 'Roses':
    if number_of_flowers > 80:
        total_price = number_of_flowers * 5 * 0.9
    else:
        total_price = number_of_flowers * 5
elif type_of_flowers == 'Dahlias':
    if number_of_flowers > 90:
        total_price = number_of_flowers * 3.8 * 0.85
    else:
        total_price = number_of_flowers * 3.8
elif type_of_flowers == 'Tulips':
    if number_of_flowers > 80:
        total_price = number_of_flowers * 2.8 * 0.85
    else:
        total_price = number_of_flowers * 2.8
elif type_of_flowers == 'Narcissus':
    if number_of_flowers < 120:
        total_price = number_of_flowers * 3 * 1.15
    else:
        total_price = number_of_flowers * 3
elif type_of_flowers == 'Gladiolus':
    if number_of_flowers < 80:
        total_price = number_of_flowers * 2.5 * 1.2
    else:
        total_price = number_of_flowers * 2.5
if budget >= total_price:
    left_money = budget - total_price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {left_money:.2f} leva left.")
else:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
