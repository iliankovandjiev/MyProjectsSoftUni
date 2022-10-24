sequence_of_numbers = input().split(', ')
int_of_numbers = list(map(int, sequence_of_numbers))
max_loop = max(int_of_numbers) // 10
loop = 1
while len(int_of_numbers) > 0:
    new_list = []
    if loop > max_loop + 1:
        break
    for num in int_of_numbers:

        if num <= (loop * 10):
            new_list.append(num)

    int_of_numbers = list(filter(lambda i: i not in new_list, int_of_numbers))
    print(f"Group of {loop * 10}'s: {new_list}")
    loop += 1
