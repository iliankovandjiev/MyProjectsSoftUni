month = int(input())
electricity = 0
water = 20
internet = 15
other = 0
average = 0
for i in range(month):
    bill_electricity = float(input())
    electricity += bill_electricity
    other += (bill_electricity + water + internet) * 1.2
water *= month
internet *= month
average = (electricity + water + internet + other) / month
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')