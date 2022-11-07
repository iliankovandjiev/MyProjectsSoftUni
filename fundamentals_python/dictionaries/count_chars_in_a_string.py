counts_all_characters = input().split()
final_string = ''.join(counts_all_characters)
characters_dict = {}
for letter in final_string:
    if letter not in characters_dict:
        characters_dict[letter] = 0
    characters_dict[letter] += 1
for char, occurrence in characters_dict.items():
    print(f'{char} -> {occurrence}')
