quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000
mount_is_passed = True
for days in range(1, 31):
    quantity_food -= 300
    if days % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if days % 3 == 0:
        quantity_cover -= guinea_weight / 3
    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        mount_is_passed = False
        break
if mount_is_passed:
    print(f"Everything is fine! Puppy is happy! Food: {(quantity_food / 1000):.2f}, Hay: {(quantity_hay / 1000):.2f}, Cover: {(quantity_cover / 1000):.2f}.")
else:
    print("Merry must go to the pet store!")