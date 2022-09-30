fuel = str(input())
litres_car = float(input())
card_member = str(input())
gasoline = 2.22
disel = 2.33
gas = 0.93
if  fuel == 'Gas':
    price = gas * litres_car
    if card_member == 'Yes':
        price = (gas - 0.08) * litres_car
    if litres_car > 25:
        price = price * 0.9
    if 25 >= litres_car > 20:
        price = price * 0.92
elif fuel == 'Gasoline':
    price = gasoline * litres_car
    if card_member == 'Yes':
        price = (gasoline - 0.18) * litres_car
    if litres_car > 25:
        price = price * 0.9
    if 25 >= litres_car > 20:
        price = price * 0.92
elif fuel == 'Diesel':
    price = disel * litres_car
    if card_member == 'Yes':
        price = (disel - 0.12) * litres_car
    if litres_car > 25:
        price = price * 0.9
    if 25 >= litres_car > 20:
        price = price * 0.92
print(f'{price:.2f} lv.')


