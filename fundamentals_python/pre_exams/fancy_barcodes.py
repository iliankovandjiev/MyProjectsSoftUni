import re

number_of_barcode = int(input())
for _ in range(number_of_barcode):
    barcode = input()
    pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
    valid_barcode = re.search(pattern, barcode)
    if valid_barcode != None:
        if re.search(r'\d', valid_barcode.group()):
            product_group = ''
            for char in valid_barcode.group():
                if char.isdigit():
                    product_group += char
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')

