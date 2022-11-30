dict_of_pieces = {}
number_of_pieces = int(input())
for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    dict_of_pieces[piece] = [composer, key]
command = input()
while command != 'Stop':
    command = command.split('|')
    if "Add" in command[0]:
        if command[1] not in dict_of_pieces.keys():
            dict_of_pieces[command[1]] = [command[2], command[3]]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f'{command[1]} is already in the collection!')
    elif "Remove" in command[0]:
        if command[1] in dict_of_pieces.keys():
            del dict_of_pieces[command[1]]
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    elif "ChangeKey" in command[0]:
        if command[1] in dict_of_pieces.keys():
            dict_of_pieces[command[1]][1] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    command = input()
for piece1 in dict_of_pieces.keys():
    print(f'{piece1} -> Composer: {dict_of_pieces[piece1][0]}, Key: {dict_of_pieces[piece1][1]}')