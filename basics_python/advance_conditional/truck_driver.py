season = input()
total_km = float(input())
total_money = 0
if total_km <= 5000:
    if season == "Spring" or season == 'Autumn':
        total_money = 4 * 0.75 * total_km
    elif season == "Summer":
        total_money = 4 * 0.90 * total_km
    elif season == "Winter":
        total_money = 4 * 1.05 * total_km
elif total_km <= 10000:
    if season == "Spring" or season == 'Autumn':
        total_money = 4 * 0.95 * total_km
    elif season == "Summer":
        total_money = 4 * 1.10 * total_km
    elif season == "Winter":
        total_money = 4 * 1.25 * total_km
else:
    total_money = 4 * 1.45 * total_km
money_after_taxes = total_money * 0.9
print(f'{money_after_taxes:.2f}')