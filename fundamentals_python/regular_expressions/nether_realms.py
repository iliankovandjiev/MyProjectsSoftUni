import re

single_line_input = (input().split(','))
damage_pattern = r'(\-?\+?[0-9]+(\.[0-9]+)?)'
health_pattern = r'[^\+\-\*\/\.0-9]'
monsters = {}
for monster in single_line_input:
    monster = monster.strip()
    total_health = 0
    total_damage = 0
    damage_symbol = re.findall(damage_pattern, monster)
    health_symbol = re.findall(health_pattern, monster)
    for damage in damage_symbol:
        total_damage += float(damage[0])
    for health in health_symbol:
        total_health += ord(health)
    for symbol in monster:
        if symbol == '*':
            total_damage *= 2
        elif symbol == '/':
            total_damage /= 2
    monsters[monster] = total_health, total_damage
sorted_monsters = sorted(monsters)
for sorted_monster in sorted_monsters:
    print(f'{sorted_monster} - {monsters[sorted_monster][0]} health, {monsters[sorted_monster][1]:.2f} damage')
