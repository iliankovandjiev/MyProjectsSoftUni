number_of_heroes = int(input())
heroes_dict = {}
for _ in range(number_of_heroes):
    heroes = input().split(' ')
    hero_name = heroes[0]
    hero_hp = int(heroes[1])
    hero_mp = int(heroes[2])
    heroes_dict[hero_name] = [hero_hp, hero_mp]
while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name][1] >= mp_needed:
            heroes_dict[hero_name][1] -= mp_needed
            mana_points_left = heroes_dict[hero_name][1]
            print(f'{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[hero_name][0] -= damage
        if heroes_dict[hero_name][0] > 0:
            current_hp = heroes_dict[hero_name][0]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        hero_name = command[1]
        amount = int(command[2])
        if (heroes_dict[hero_name][1] + amount) > 200:
            amount_recovered = 200 - heroes_dict[hero_name][1]
            heroes_dict[hero_name][1] = 200
        else:
            amount_recovered = amount
            heroes_dict[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif command[0] == 'Heal':
        hero_name = command[1]
        amount = int(command[2])
        if (heroes_dict[hero_name][0] + amount) > 100:
            amount_recovered = 100 - heroes_dict[hero_name][0]
            heroes_dict[hero_name][0] = 100
        else:
            amount_recovered = amount
            heroes_dict[hero_name][0] += amount
        print(f"{hero_name} healed for {amount_recovered} HP!")
for hero in heroes_dict.keys():
    print(f"{hero}\nHP: {heroes_dict[hero][0]}\nMP: {heroes_dict[hero][1]}")

