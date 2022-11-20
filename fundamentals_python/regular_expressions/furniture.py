import re

all_furniture = []
total_money = 0
purchase = input()
while purchase != 'Purchase':
    pattern = r'>>([A-Za-z]+)<<([0-9]+\.?[0-9]+)\!([0-9]+)'
    valid_information = re.search(pattern, purchase)
    if valid_information:
        furniture, price, quantity = valid_information.groups()
        all_furniture.append(furniture)
        total_money += float(price) * int(quantity)
    purchase = input()

print('Bought furniture:')
for item in all_furniture:
    print(item)
print(f'Total money spend: {total_money:.2f}')
