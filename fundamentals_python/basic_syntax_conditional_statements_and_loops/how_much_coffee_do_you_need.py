command_input = input()
coffe_count = 0
sleep_needed = False
while command_input != 'END':
    if command_input == 'coding' or command_input == 'dog' or command_input == 'cat' or command_input == 'movie':
        coffe_count += 1
    elif command_input == 'CODING' or command_input == 'DOG' or command_input == 'CAT' or command_input == 'MOVIE':
        coffe_count += 2
    if coffe_count > 5:
        print('You need extra sleep')
        sleep_needed = True
        break
    command_input = input()
if not sleep_needed:
    print(coffe_count)

