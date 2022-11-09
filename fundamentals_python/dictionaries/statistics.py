commands = input()
products = {}
while True:
    if commands == 'statistics':
        break
    product, quantity = commands.split(': ')
    if product not in products.keys():
        products[product] = 0
    products[product] += int(quantity)
    commands = input()
print("Products in stock:")
for product1, quantity1 in products.items():
    print(f'- {product1}: {quantity1}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
