product = input()
quantity = float(input())


def total_price():
    if product == 'coffee':
        result = 1.50 * quantity
        return f'{result:.2f}'
    elif product == 'coke':
        result = 1.40 * quantity
        return f'{result:.2f}'
    elif product == 'water':
        result = 1.00 * quantity
        return f'{result:.2f}'
    elif product == 'snacks':
        result = 2.00 * quantity
        return f'{result:.2f}'


print(total_price())
