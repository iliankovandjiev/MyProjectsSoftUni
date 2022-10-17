numbers = input().split(' ')
int_numbers = [int(x) for x in numbers]
average_number = sum(int_numbers) / len(int_numbers)
new_list = []
final_list = []
for num in int_numbers:
    if num > average_number:
        new_list.append(num)
if len(new_list) == 0:
    print('No')
else:
    if len(new_list) > 4:
        new_list = sorted(new_list, reverse=True)
        result = [str(x) for x in new_list]
        for num in range(5):
            final_list.append(result[num])
        print(' '.join(final_list))

    else:
        new_list = sorted(new_list, reverse=True)
        result = [str(x) for x in new_list]
        print(' '.join(result))
