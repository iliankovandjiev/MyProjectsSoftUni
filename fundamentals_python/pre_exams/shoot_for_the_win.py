sequence_of_integer = input().split(' ')
lst_of_integer = [int(num) for num in sequence_of_integer]
count = 0
while True:
    command = input()
    if command == 'End':
        break
    if int(command) < len(lst_of_integer):
        index = int(command)
        for num in range(len(lst_of_integer)):
            if lst_of_integer[num] <= lst_of_integer[index] and lst_of_integer[num] != -1 and num != index:
                lst_of_integer[num] += lst_of_integer[index]

            elif lst_of_integer[num] > lst_of_integer[index] and lst_of_integer[num] != -1 and num != index:
                lst_of_integer[num] -= lst_of_integer[index]
        count += 1
    lst_of_integer[index] = -1
printed_list = ' '.join([str(num) for num in lst_of_integer])
print(f'Shot targets: {count} -> {printed_list}')
