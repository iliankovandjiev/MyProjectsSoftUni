def add_func(first_element, groceries):
    if first_element not in groceries:
        groceries.insert(0, first_element)
    return groceries


def remove_func(first_element, groceries):
    if first_element in groceries:
        groceries.remove(first_element)
    return groceries


def change_func(first_element, second_element, groceries):
    if first_element in groceries:
        index = groceries.index(first_element)
        groceries[index] = second_element
    return groceries


def rearrange_func(first_element, groceries):
    if first_element in groceries:
        groceries.remove(first_element)
        groceries.append(first_element)
    return groceries


def groceries_func(groceries):
    while True:
        command = input()
        if command == "Go Shopping!":
            break
        if 'Urgent' in command:
            action, item = command.split(' ')
            add_func(item, groceries)
        elif 'Unnecessary' in command:
            action, item = command.split(' ')
            remove_func(item, groceries)
        elif 'Correct' in command:
            action, item, new_item = command.split(' ')
            change_func(item, new_item, groceries)
        elif 'Rearrange' in command:
            action, item = command.split(' ')
            rearrange_func(item, groceries)

    result = ', '.join(str(lst) for lst in groceries)
    print(result)


groceries_list = input().split('!')
groceries_func(groceries_list)
