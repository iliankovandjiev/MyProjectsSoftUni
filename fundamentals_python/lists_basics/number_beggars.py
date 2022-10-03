list_of_numbers = input().split(', ')
count_of_beggars = int(input())
list_of_numbers_as_digits = []
final_list = []
counter = 0
for element in list_of_numbers:
    list_of_numbers_as_digits.append(int(element))
while counter < count_of_beggars:
    sum_of_numbers = 0
    for current_index in range(counter, len(list_of_numbers), count_of_beggars):
        sum_of_numbers += list_of_numbers_as_digits[current_index]
    final_list.append(sum_of_numbers)
    counter += 1
print(final_list)




