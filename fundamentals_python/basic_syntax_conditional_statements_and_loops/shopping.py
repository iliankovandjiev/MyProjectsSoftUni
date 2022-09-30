budget = int(input())
left_budget = True
while budget >= 0:
    price_product = input()
    if price_product == 'End':
        print('You bought everything needed.')
        break
    else:
        price_product = int(price_product)
        budget -= price_product
        if budget < 0:
            left_budget = False
if not left_budget:
    print('You went in overdraft!')