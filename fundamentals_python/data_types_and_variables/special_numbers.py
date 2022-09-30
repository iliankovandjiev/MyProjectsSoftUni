n_numbers = int(input())
for current_number in range(1, n_numbers + 1):
    sum_num = 0
    is_special = False
    current_number = str(current_number)
    for i in range(len(current_number)):
        sum_num += int(current_number[i])
    if sum_num == 5 or sum_num == 7 or sum_num == 11:
        is_special = True
    print(f'{current_number} -> {is_special}')
