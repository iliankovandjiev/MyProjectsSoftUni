number_of_cars = int(input())
total_cars = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    total_cars[car] = [int(mileage), int(fuel)]
command = input()
while command != 'Stop':
    command = command.split(' : ')
    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if total_cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            total_cars[car][0] += distance
            total_cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if total_cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del total_cars[car]
    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        if (total_cars[car][1] + fuel) > 75:
            refueled = 75 - total_cars[car][1]
            total_cars[car][1] = 75
        else:
            total_cars[car][1] += fuel
            refueled = fuel
        print(f"{car} refueled with {refueled} liters")
    elif command[0] == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        total_cars[car][0] -= kilometers
        if total_cars[car][0] < 10000:
            total_cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()
for car in total_cars.keys():
    fuel = total_cars[car][1]
    mileage = total_cars[car][0]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")