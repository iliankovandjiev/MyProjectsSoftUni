total_play = int(input())
result = 0
range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0
range6 = 0
for i in range(total_play):
    num_input = int(input())
    if 0 <= num_input <= 9:
        result += 0.2 * num_input
        range1 += 1
    elif 10 <= num_input <= 19:
        result += 0.3 * num_input
        range2 += 1
    elif 20 <= num_input <= 29:
        result += 0.4 * num_input
        range3 += 1
    elif 30 <= num_input <= 39:
        result += 50
        range4 += 1
    elif 40 <= num_input <= 50:
        result += 100
        range5 += 1
    else:
        result = result / 2
        range6 += 1
per_range1 = range1 / total_play * 100
per_range2 = range2 / total_play * 100
per_range3 = range3 / total_play * 100
per_range4 = range4 / total_play * 100
per_range5 = range5 / total_play * 100
per_range6 = range6 / total_play * 100
print(f'{result:.2f}')
print(f'From 0 to 9: {per_range1:.2f}%')
print(f'From 10 to 19: {per_range2:.2f}%')
print(f'From 20 to 29: {per_range3:.2f}%')
print(f'From 30 to 39: {per_range4:.2f}%')
print(f'From 40 to 50: {per_range5:.2f}%')
print(f'Invalid numbers: {per_range6:.2f}%')