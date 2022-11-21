import re

list_of_participants = input().split(', ')
command = input()
pattern = r'[a-zA-Z0-9]'
participants_results = {}
while command != 'end of race':
    name = ''
    distance = 0
    characters = re.findall(pattern, command)
    for char in characters:
        if char.isdigit():
            distance += int(char)
        else:
            name += char
    if name in list_of_participants:
        if name not in participants_results:
            participants_results[name] = 0
        participants_results[name] += distance

    command = input()
place = 0
sorted_dictionary = sorted(participants_results.items(), key=lambda x: x[1], reverse=True)
for score in sorted_dictionary:
    place += 1
    if place == 1:
        print(f'{place}st place: {sorted_dictionary[place - 1][0]}')
    elif place == 2:
        print(f'{place}nd place: {sorted_dictionary[place - 1][0]}')
    elif place == 3:
        print(f'{place}rd place: {sorted_dictionary[place - 1][0]}')