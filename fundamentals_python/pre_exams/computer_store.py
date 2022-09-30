component_price = input()
price_without_taxes = 0
taxes = 0
total_price = 0

while True:
    if component_price == 'special' or component_price == 'regular':
        break
    if float(component_price) <= 0:
        print('Invalid price!')
    else:
        price_without_taxes += float(component_price)
    component_price = input()
if price_without_taxes == 0:
    print('Invalid order!')
else:
    if component_price == 'special':
        taxes = 0.2 * price_without_taxes
        total_price = 0.9 * (taxes + price_without_taxes)
    elif component_price == 'regular':
        taxes = 0.2 * price_without_taxes
        total_price = (taxes + price_without_taxes)

    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')