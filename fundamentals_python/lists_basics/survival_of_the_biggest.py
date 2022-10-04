list_of_numbers = input().split()
count_of_number_to_remove = int(input())
new_list_of_numbers = []
final_numbers = ''
counter = 0
for index in range(len(list_of_numbers)):
    new_list_of_numbers.append(int(list_of_numbers[index]))
for small in range(count_of_number_to_remove):
    new_list_of_numbers.remove(min(new_list_of_numbers))
for string in new_list_of_numbers:
    print(string, end='')
    counter += 1
    while counter < len(new_list_of_numbers):
        print(', ', end='')
        break