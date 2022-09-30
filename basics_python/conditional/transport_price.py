kilometers = int(input())
day_night = str(input())
taxi = 0
autobus = 0
train = 0
if day_night == str('day'):
    taxi = 0.7 + 0.79 * kilometers
else:
    taxi = 0.7 + 0.9 * kilometers
if kilometers >= 100:
    autobus = 0.09 * kilometers
    train = 0.06 * kilometers
elif kilometers >= 20:
    autobus = 0.09 * kilometers
if autobus == 0:
    print(f'{taxi:.2f}')
elif train == 0:
    print(f'{min(taxi, autobus):.2f}')
else:
    print(f'{min(taxi, autobus, train):.2f}')


