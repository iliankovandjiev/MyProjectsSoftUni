tipe_of_fuel = str(input())
litres_car = float(input())
if tipe_of_fuel == 'Diesel' or tipe_of_fuel == 'Gasoline' or tipe_of_fuel == 'Gas':
    if litres_car >= 25:
        print(f"You have enough {(tipe_of_fuel.lower())}.")
    else:
        print(f'Fill your tank with {tipe_of_fuel.lower()}!')
else:
    print('Invalid fuel!')