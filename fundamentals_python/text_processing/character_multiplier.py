first_string, second_sting = input().split()
total_sum = 0
if len(first_string) == len(second_sting):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_sting[index])
elif len(first_string) > len(second_sting):
    for index in range(len(second_sting)):
        total_sum += ord(first_string[index]) * ord(second_sting[index])
    for second_index in range(len(second_sting), len(first_string)):
        total_sum += ord(first_string[second_index])
else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_sting[index])
    for second_index in range(len(first_string), len(second_sting)):
        total_sum += ord(second_sting[second_index])
print(total_sum)

