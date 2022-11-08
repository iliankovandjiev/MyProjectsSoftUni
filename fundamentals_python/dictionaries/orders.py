products = {}
command = input().split()
while True:
    if command == ['buy']:
        break
    else:
        name, price, quantity = command[0], command[1], command[2]
        if name not in products.keys():
            products[name] = [0, 0]
        products[name][0] = float(price)
        products[name][1] += int(quantity)
        command = input().split()
for product in products:
    a = products[product][0]
    b = products[product][1]
    mult_a = float(a)
    mult_b = float(b)
    total_price = mult_b * mult_a
    print(f"{product} -> {total_price:.2f}")






# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy