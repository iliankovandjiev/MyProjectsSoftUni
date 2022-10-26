def add_func(value, numbers):
    numbers.append(value)
    return numbers


def remove_func(value, numbers):
    numbers.remove(value)
    return numbers


def replace_func(value, replacement, numbers):
    index = numbers.index(value)
    if 0 <= index < len(numbers):
        numbers.remove(value)
        numbers.insert(index, replacement)
    return numbers


def collapse_func(value, numbers):
    numbers = [num for num in numbers if num > value]
    return numbers


def modify_func(numbers):
    while True:
        command = input()
        if command == 'Finish':
            break
        if 'Add' in command:
            add_command, value = command.split()
            add_func(int(value), numbers)
        elif 'Remove' in command:
            remove_command, value = command.split()
            remove_func(int(value), numbers)
        elif 'Replace' in command:
            replace_command, value, replacement = command.split()
            replace_func(int(value), int(replacement), numbers)
        elif 'Collapse' in command:
            collapse_command, value = command.split()
            collapse_func(int(value), numbers)
    print(' '.join(list(map(str, numbers))))


number_sequence = input().split()
number_sequence = list(map(int, number_sequence))
modify_func(number_sequence)
