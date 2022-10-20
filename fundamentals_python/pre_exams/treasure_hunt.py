def loot_func(items, loot):
    for new_items in items:

        if new_items not in loot:
            loot.insert(0, new_items)


    return loot


def drop_func(index, loot):
    if 0 <= index <= len(loot):

        if len(loot) > 0:
            item_drop = loot.pop(index)
            loot.append(item_drop)
            return loot

    return loot


def count_func(count, loot):
    stolen_list = []

    if count >= len(loot):
        stolen_list = loot
        print(', '.join(stolen_list))
        loot.clear()
    else:
        for i in range(count):
            stolen_item = loot.pop()
            stolen_list.append(stolen_item)
            reversed_list = stolen_list[::-1]
        print(', '.join(reversed_list))
    return loot


def treasure_chest(loot):
    average_treasure_gain = 0
    treasure_gain = 0

    while True:
        command = input()

        if command == "Yohoho!":
            break
        command_list = command.split(' ')

        if 'Loot' in command_list[0]:
            command_list.remove('Loot')
            loot_func(command_list, loot)

        elif 'Drop' in command_list[0]:
            index = int(command_list[1])
            drop_func(index, loot)

        elif 'Steal' in command_list[0]:
            count = int(command_list[1])
            count_func(count, loot)

    if len(loot) != 0:

        for treasure in loot:
            treasure_gain += len(treasure)

        average_treasure_gain = treasure_gain / len(loot)
        print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')

    else:
        print("Failed treasure hunt.")


initial_loot = input().split('|')
treasure_chest(initial_loot)

