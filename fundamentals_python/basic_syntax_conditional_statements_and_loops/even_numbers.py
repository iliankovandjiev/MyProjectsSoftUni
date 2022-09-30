n_numbers = int(input())
for i in range(n_numbers):
    new_number = int(input())
    if new_number % 2 != 0:
        print(f'{new_number} is odd!')
        break
else:
    print('All numbers are even.')