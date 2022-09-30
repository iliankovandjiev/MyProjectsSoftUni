num_junior = int(input())
num_senior = int(input())
type_of_road = input()
total_tax = 0
donate_tax = 0
if type_of_road == 'trail':
    total_tax = num_junior * 5.5 + num_senior * 7
elif type_of_road == 'cross-country':
    total_tax = num_junior * 8 + num_senior * 9.5
    if num_senior + num_junior >= 50:
        total_tax *= 0.75
elif type_of_road == 'downhill':
    total_tax = num_junior * 12.25 + num_senior * 13.75
elif type_of_road == 'road':
    total_tax = num_junior * 20 + num_senior * 21.5

donate_tax = 0.95 * total_tax
print(f'{donate_tax:.2f}')
