numbers = input().split(' ')
int_numbers = [int(x) for x in numbers]
average_number = sum(int_numbers) / len(int_numbers)
new_list = []
final_list = []
for num in int_numbers:
    if num > average_number:
        new_list.append(num)
if new_list == 0:
    print('No')
else:
    if len(new_list) > 5:
        for num in range(5):
            final_list.append(new_list[num])
        result = [str(x) for x in final_list]
        print(' '.join(result))














# if len(int_numbers) < 5:
#     print('less than 5 numbers')
