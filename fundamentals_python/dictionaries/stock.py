input_line = input().split(' ')
bakery = {}
for index in range(0, len(input_line), 2):
    keys = input_line[index]
    value = input_line[index + 1]
    bakery[keys] = int(value)
searched_product = input().split()
for product in searched_product:
    if product in bakery:
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        pass

