num_chry = int(input())
num_roses = int(input())
num_tulip = int(input())
season = input()
festival = input()
total_sum = 0
if festival == 'Y':
    if season == 'Spring' or season == 'Summer':
        total_sum = num_chry * 2 + num_roses * 4.1 + num_tulip * 2.5
        total_sum *= 1.15
        if num_tulip > 7 and season == 'Spring':
            total_sum *= 0.95
        if num_chry + num_roses + num_tulip > 20:
            total_sum *= 0.8
        total_sum += 2
    elif season == 'Autumn' or season == 'Winter':
        total_sum = num_chry * 3.75 + num_roses * 4.5 + num_tulip * 4.15
        total_sum *= 1.15
        if num_roses >= 10 and season == 'Winter':
            total_sum *= 0.90
        if num_chry + num_roses + num_tulip > 20:
            total_sum *= 0.8
        total_sum += 2
elif festival == 'N':
    if season == 'Spring' or season == 'Summer':
        total_sum = num_chry * 2 + num_roses * 4.1 + num_tulip * 2.5
        if num_tulip > 7 and season == 'Spring':
            total_sum *= 0.95
        if num_chry + num_roses + num_tulip > 20:
            total_sum *= 0.8
        total_sum += 2
    elif season == 'Autumn' or season == 'Winter':
        total_sum = num_chry * 3.75 + num_roses * 4.5 + num_tulip * 4.15
        if num_roses >= 10 and season == 'Winter':
            total_sum *= 0.90
        if num_chry + num_roses + num_tulip > 20:
            total_sum *= 0.8
        total_sum += 2
print(f'{total_sum:.2f}')
