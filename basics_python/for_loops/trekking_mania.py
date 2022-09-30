n_groups = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
total_people = 0
for _ in range(n_groups):
    num_people = int(input())
    total_people += num_people
    if num_people <= 5:
        group1 += num_people
    elif num_people <= 12:
        group2 += num_people
    elif num_people <= 25:
        group3 += num_people
    elif num_people <= 40:
        group4 += num_people
    else:
        group5 += num_people

perc_group1 = group1 / total_people * 100
perc_group2 = group2 / total_people * 100
perc_group3 = group3 / total_people * 100
perc_group4 = group4 / total_people * 100
perc_group5 = group5 / total_people * 100
print(f'{perc_group1:.2f}%')
print(f'{perc_group2:.2f}%')
print(f'{perc_group3:.2f}%')
print(f'{perc_group4:.2f}%')
print(f'{perc_group5:.2f}%')
