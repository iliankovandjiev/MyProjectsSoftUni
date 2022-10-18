initial_energy = int(input())
total_energy = initial_energy
count_wins = 0
energy_left = True
while True:
    command_distance = input()
    if command_distance == 'End of battle':
        break
    if int(command_distance) <= total_energy:
        total_energy -= int(command_distance)
        count_wins += 1
        if count_wins % 3 == 0:
            total_energy += count_wins
    else:
        energy_left = False
        break
if energy_left:
    print(f"Won battles: {count_wins}. Energy left: {total_energy}" )
else:
    print(f'Not enough energy! Game ends with {count_wins} won battles and {total_energy} energy')