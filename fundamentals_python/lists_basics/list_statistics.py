number_input = int(input())
lst_numbers_negative = []
lst_numbers_positive = []
for numbers in range(number_input):
    new_number = int(input())
    if new_number < 0:
        lst_numbers_negative.append(new_number)
    else:
        lst_numbers_positive.append(new_number)
print(lst_numbers_positive)
print(lst_numbers_negative)
print(f"Count of positives: {len(lst_numbers_positive)}")
print(f'Sum of negatives: {sum(lst_numbers_negative)}')
