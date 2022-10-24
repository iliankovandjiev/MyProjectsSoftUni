input_strings = input().split()
while True:
    command = input()
    if command == '3:1':
        break
    if 'merge' in command:
        merge, start_index, end_index = command.split()
        merge_fun()

    elif 'divide' in command:
        divide, index, partitions = command.split()
