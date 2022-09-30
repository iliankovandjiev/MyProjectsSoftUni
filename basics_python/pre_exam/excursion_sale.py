excursion_sea = int(input())
excursion_mountain = int(input())
command = input()
total_price = 0
counter_sea = 0
counter_mountain = 0
all_its_sold = False
while command != 'Stop':
    if command == 'sea' and counter_sea < excursion_sea:
        counter_sea += 1
    elif command == 'mountain' and counter_mountain < excursion_mountain:
        counter_mountain += 1
    if counter_sea >= excursion_sea and counter_mountain >= excursion_mountain:
        all_its_sold = True
        break
    command = input()
total_price = counter_sea * 680 + counter_mountain * 499
if all_its_sold:
    print(f'Good job! Everything is sold.')
    print(f'Profit: {total_price:.0f} leva.')
else:
    print(f'Profit: {total_price:.0f} leva.')