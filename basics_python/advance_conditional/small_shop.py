product = str(input())
city = str(input())
quantity = float(input())
price = 0
if city == 'Sofia':
    if product == 'coffee':
        price = 0.5 * quantity
    elif product == 'water':
        price = 0.8 * quantity
    elif product == 'beer':
        price = 1.2 * quantity
    elif product == 'sweets':
        price = 1.45 * quantity
    elif product == 'peanuts':
        price = 1.6 * quantity
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.4 * quantity
    elif product == 'water':
        price = 0.7 * quantity
    elif product == 'beer':
        price = 1.15 * quantity
    elif product == 'sweets':
        price = 1.3 * quantity
    elif product == 'peanuts':
        price = 1.5 * quantity
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45 * quantity
    elif product == 'water':
        price = 0.7 * quantity
    elif product == 'beer':
        price = 1.1 * quantity
    elif product == 'sweets':
        price = 1.35 * quantity
    elif product == 'peanuts':
        price = 1.55 * quantity
print(price)
