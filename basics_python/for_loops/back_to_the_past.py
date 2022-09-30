money = float(input())
year = int(input())
money_needed = 0
for i in range (1800, year+1):
    n = i - 1800
    if i % 2 == 0:
        money_needed += 12000
    else:
        money_needed += (12000 + 50 * (18 + n))
if money >= money_needed:
    diff = money - money_needed
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    diff1 = money_needed - money
    print(f'He will need {diff1:.2f} dollars to survive.')
