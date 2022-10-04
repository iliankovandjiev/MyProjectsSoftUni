total_energy = 100
total_coins = 100
work_day_event = input().split('|')
factory_is_open = True
for event in work_day_event:
    lst_of_event = event.split('-')
    command_is = lst_of_event[0]
    number_is = int(lst_of_event[1])
    if command_is == 'rest':
        current_energy = total_energy
        total_energy += number_is
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f"Current energy: {total_energy}.")
    elif command_is == 'order':

        if total_energy >= 30:
            total_energy -= 30
            total_coins += number_is
            print(f'You earned {number_is} coins.')
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= number_is:
            total_coins -= number_is
            print(f"You bought {command_is}.")
        else:
            factory_is_open = False
            print(f"Closed! Cannot afford {command_is}.")
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
