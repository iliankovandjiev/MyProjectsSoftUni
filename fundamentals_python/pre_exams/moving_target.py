sequence_of_target = input().split()
integer_of_sequence_of_target = [int(num) for num in sequence_of_target]
final_integer = integer_of_sequence_of_target
while True:
    command = input()
    if command == "End":
        break
    command_one, index, value = command.split(' ')
    if command_one == 'Shoot':
        index = int(index)
        value = int(value)
        if index < len(final_integer):
            final_integer[index] -= value
            if final_integer[index] <= 0:
                final_integer.pop(index)
                # print(final_integer)
    elif command_one == 'Add':
        index = int(index)
        value = int(value)
        if index < len(final_integer):
            final_integer.insert(index, value)
        else:
            print("Invalid placement!")
    elif command_one == 'Strike':
        index = int(index)
        value = int(value)
        if index in range(len(final_integer)) and (index - value) in range(len(final_integer)) and (index + value) in range(len(final_integer)):
            if (value * 2 + 1) < len(final_integer):
                for num in range((index - value), (index + value + 1)):
                    final_integer.pop((index - value))
        else:
            print("Strike missed!")
print("|".join([str(num) for num in final_integer]))