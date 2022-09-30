vacation = float(input())
start_money = float(input())
total_money = start_money
day_spend = 0
total_day = 0
spend = False
while total_money < vacation:
    if day_spend == 5:
        spend = True
        break
    spend_save = input()
    actual_money = float(input())
    total_day += 1
    if spend_save == "spend":
        total_money -= actual_money
        day_spend += 1
        if total_money < 0:
            total_money = 0
    elif spend_save == 'save':
        total_money += actual_money
        day_spend = 0
if spend:
    print(f"You can't save the money.")
    print(total_day)
else:
    print(f"You saved the money for {total_day} days.")




