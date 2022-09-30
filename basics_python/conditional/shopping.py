budget_petur = float(input())
video_card = int(input())
core = int(input())
ram = int(input())
price_video_card = video_card * 250
price_core = price_video_card * 0.35
price_ram = price_video_card * 0.1
total_sum = price_video_card + price_core * core + price_ram * ram
if video_card > core:
    total_sum = total_sum * 0.85
if total_sum <= budget_petur:
    money_left = budget_petur - total_sum
    print(f'You have {money_left:.2f} leva left!')
else:
    needed_money = total_sum - budget_petur
    print(f'Not enough money! You need {needed_money:.2f} leva more!')
