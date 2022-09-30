total_money_needed = int(input())
comm_input = input()
count = 0
count_cash = 0
count_card = 0
total_money_card = 0
total_money_cash = 0
total_money = 0
money_collected = False
while comm_input != 'End':
    comm_input = int(comm_input)
    count += 1
    if count % 2 == 0:
        if comm_input < 10:
            print(f'Error in transaction!')
        else:
            print('Product sold!')
            count_card += 1
            total_money_card += comm_input
            total_money += comm_input
    else:
        if comm_input > 100:
            print(f'Error in transaction!')
        else:
            print('Product sold!')
            count_cash += 1
            total_money_cash += comm_input
            total_money += comm_input
    if total_money >= total_money_needed:
        money_collected = True
        break
    else:
        comm_input = input()
if money_collected:
    print(f'Average CS: {(total_money_cash / count_cash):.2f}')
    print(f'Average CC: {(total_money_card / count_card):.2f}')
else:
    print(f'Failed to collect required money for charity.')



