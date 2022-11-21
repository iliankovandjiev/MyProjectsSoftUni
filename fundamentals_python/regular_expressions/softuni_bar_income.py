import re

command = input()
pattern_name = r'\%\b([A-Z][a-z]+)\b\%'
pattern_product = r'\<(\w+)\>'
pattern_count = r'\|([0-9]+)\|'
pattern_price = r'([0-9]+\.?[0-9]+)\$'
total_income = 0
while command != 'end of shift':
    valid_name = re.findall(pattern_name, command)
    valid_product = re.findall(pattern_product, command)
    valid_count = re.findall(pattern_count, command)
    valid_price = re.findall(pattern_price, command)
    if valid_name and valid_product and valid_count and valid_price:
        total_price = int(valid_count[0]) * float(valid_price[0])
        print(f'{valid_name[0]}: {valid_product[0]} - {total_price:.2f}')
        total_income += total_price
    command = input()
print(f'Total income: {total_income:.2f}')