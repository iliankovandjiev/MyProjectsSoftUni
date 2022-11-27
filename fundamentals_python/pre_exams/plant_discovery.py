number_of_lines = int(input())
new_plants = {}
for _ in range(number_of_lines):
    information_about_plant = input().split('<->')
    new_plants[information_about_plant[0]] = [information_about_plant[1], []]
command = input()
while command != 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        plant, rating = command[1]. split(' - ')
        if plant in new_plants.keys():
            new_plants[plant][1].append(int(rating))
        else:
            print('error')
    elif command[0] == 'Update':
        plant, rarity = command[1]. split(' - ')
        if plant in new_plants.keys():
            new_plants[plant][0] = rarity
        else:
            print('error')
    elif command[0] == 'Reset':
        plant = command[1]
        if plant in new_plants.keys():
            new_plants[plant][1].pop()
        else:
            print('error')
    else:
        print('error')
    command = input()
print("Plants for the exhibition:")
for plant_name in new_plants.keys():
    rarity = new_plants[plant_name][0]
    if len(new_plants[plant_name][1]) != 0:
        average_rating = sum(new_plants[plant_name][1]) / len(new_plants[plant_name][1])
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")

