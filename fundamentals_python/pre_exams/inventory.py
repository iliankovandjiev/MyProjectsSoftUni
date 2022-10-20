def collect_func(item, items):
    if item not in items:
        items.append(item)
        return items
    return items


def drop_func(item, items):
    if item in items:
        items.remove(item)
        return items
    return items


def combine_fun(item, items):
    old_item, new_item = item.split(':')
    if old_item in items:
        index_old_item = items.index(old_item)
        items.insert((index_old_item + 1), new_item)
        return items
    return items


def renew_func(item, items):
    if item in items:
        items.remove(item)
        items.append(item)
        return items
    return items


def gather_craft_items(items):
    while True:
        commands = input()

        if commands == 'Craft!':
            break

        action, item = commands.split(' - ')

        if action == 'Collect':
            collect_func(item, items)

        elif action == 'Drop':
            drop_func(item, items)

        elif action == 'Combine Items':
            combine_fun(item, items)

        elif action == 'Renew':
            renew_func(item, items)

    print(', '.join(items))


collecting_items = input().split(', ')
gather_craft_items(collecting_items)
