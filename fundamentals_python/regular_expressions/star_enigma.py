import re

planet_name_pattern = r'@([A-Za-z]+)'
population_pattern = r':([1-9][0-9]*+)'
attack_type_pattern = r'!([A|D])!'
soldier_count_pattern = r'\-\>([1-9][0-9]*+)'
numbers_of_massages = int(input())
attacked_planets = 0
destroyed_planets = 0
attacked_planet_name = []
destroyed_planet_name = []
for num in range(numbers_of_massages):
    encrypted_message = input()
    decryption_pattern = r'[star]'
    decryption_key = len(re.findall(decryption_pattern, encrypted_message, flags=re.IGNORECASE))
    decrypted_message = ''
    for symbol in encrypted_message:
        new_symbol = chr(ord(symbol) - decryption_key)
        decrypted_message += new_symbol
    planet_name = re.findall(planet_name_pattern, decrypted_message)
    population = re.findall(population_pattern, decrypted_message)
    attack_type = re.findall(attack_type_pattern, decrypted_message)
    soldier_count = re.findall(soldier_count_pattern, decrypted_message)
    if planet_name and population and attack_type and soldier_count:
        if "A" in attack_type:
            attacked_planets += 1
            attacked_planet_name.append(planet_name)
        else:
            destroyed_planets += 1
            destroyed_planet_name.append(planet_name)
print(f'Attacked planets: {attacked_planets}')
for planet in sorted(attacked_planet_name):
    print(f"-> {planet[0]}")
print(f'Destroyed planets: {destroyed_planets}')
for planet in sorted(destroyed_planet_name):
    print(f"-> {planet[0]}")


