number_of_order = int(input())
total_price = 0
for i in range(number_of_order):
    price = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        price = days * capsules_needed_per_day * price_per_capsule
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')