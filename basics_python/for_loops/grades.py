num_student = int(input())
range2_3 = 0
range3_4 = 0
range4_5 = 0
range5_6 = 0
med_eva = 0
for i in range(num_student):
    evaluation = float(input())
    if evaluation < 3:
        range2_3 += 1
        med_eva += evaluation
    elif evaluation < 4:
        range3_4 += 1
        med_eva += evaluation
    elif evaluation < 5:
        range4_5 += 1
        med_eva += evaluation
    else:
        range5_6 += 1
        med_eva += evaluation
average_eva = med_eva / num_student
per_range2_3 = range2_3 / num_student * 100
per_range3_4 = range3_4 / num_student * 100
per_range4_5 = range4_5 / num_student * 100
per_range5_6 = range5_6 / num_student * 100
print(f'Top students: {per_range5_6:.2f}%')
print(f'Between 4.00 and 4.99: {per_range4_5:.2f}%')
print(f'Between 3.00 and 3.99: {per_range3_4:.2f}%')
print(f'Fail: {per_range2_3:.2f}%')
print(f'Average: {average_eva:.2f}')


