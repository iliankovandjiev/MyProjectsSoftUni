initial_health = 100
initial_bitcoins = 0
dungeon_rooms = input().split('|')
counter = 0
alive = True
for room in dungeon_rooms:
    counter += 1
    command, num = room.split(' ')
    if command == 'potion':
        current_health = initial_health
        initial_health += int(num)
        if initial_health >= 100:
            initial_health = 100
        heal_hp = initial_health - current_health
        print(f"You healed for {heal_hp} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == 'chest':
        initial_bitcoins += int(num)
        print(f'You found {num} bitcoins.')
    else:
        initial_health -= int(num)
        if initial_health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            alive = False
            break
if alive:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
