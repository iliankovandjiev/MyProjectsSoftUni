budget = float(input())
price_flout = float(input())
pack_eggs = 0.75 * price_flout
litre_milk = 1.25 * price_flout
current_bread_count = 0
bread_price = price_flout + pack_eggs + 0.25 * litre_milk
left_budget = budget
eggs = 0
while (left_budget - bread_price) > 0:
    current_bread_count += 1
    left_budget -= bread_price
    eggs += 3
    if current_bread_count % 3 == 0:
        eggs -= (current_bread_count - 2)
print(f'You made {current_bread_count} loaves of Easter bread! Now you have {eggs} eggs and {left_budget:.2f}BGN left.')