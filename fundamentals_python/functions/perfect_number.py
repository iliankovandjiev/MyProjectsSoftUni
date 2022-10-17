def perfect_number(numbers):
    num_sum = 0
    for num in range(1, numbers):
        if numbers % num == 0:
            num_sum += int(num)
    return num_sum


positive_integer = int(input())
total_sum = perfect_number(positive_integer)
if total_sum == positive_integer:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
