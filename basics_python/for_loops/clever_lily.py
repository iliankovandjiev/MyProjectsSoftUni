n = int(input())
washing_mashine = float(input())
price_toys = int(input())
money = 0
toys = 0
money_save = 0
for i in range(1, n+1):
    if i % 2 == 0:
        money += 10 * i / 2
    else:
        toys += 1
money_save = money - n // 2
money_save += (toys * price_toys)
if money_save >= washing_mashine:
    money_left = money_save - washing_mashine
    print(f'Yes! {money_left:.2f}')
else:
    money_need = washing_mashine - money_save
    print(f'No! {money_need:.2f}')
