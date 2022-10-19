def validation(index, item):
    if item[index] != 0:
        item[index] -= 2
        if item[index] <= 0:
            print(f"Place {index} has Valentine's day.")
    else:
        print(f"Place {index} already had Valentine's day.")


def love(item):
    index = 0
    counter = 0
    while True:
        command = input()
        if command == 'Love!':
            break
        jump, length = command.split(' ')
        index += int(length)
        if index < len(item):
            validation(index, item)
        else:
            index = 0
            validation(index, item)

    print(f"Cupid's last position was {index}.")
    for num in item:
        if num == 0:
            counter += 1

    if counter == len(item):
        print("Mission was successful.")
    else:
        house_count = len(item) - counter
        print(f"Cupid has failed {house_count} places.")


even_integer = list(map(int, input().split('@')))
love(even_integer)
