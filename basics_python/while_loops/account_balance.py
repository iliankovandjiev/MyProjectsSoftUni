cash = input()
total_cash = 0
while cash != 'NoMoreMoney':
    amount = float(cash)
    if amount < 0:
        print(f'Invalid operation!')
        cash = 'NoMoreMoney'
    else:
        total_cash += amount
        print(f'Increase: {amount:.2f}')
        cash = input()
print(f'Total: {total_cash:.2f}')