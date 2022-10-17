elements = input().split(' ')
new_elements = [int(element) for element in elements]
command = input()
while command != 'end':
    if 'swap' in command:
        indexes = command.split(' ')
        index_one = int(indexes[1])
        index_two = int(indexes[2])
        new_elements[index_one], new_elements[index_two] = new_elements[index_two], new_elements[index_one]
    elif 'multiply' in command:
        indexes = command.split(' ')
        index_one = int(indexes[1])
        index_two = int(indexes[2])
        new_elements[index_one] = new_elements[index_two] * new_elements[index_one]
    elif 'decrease' in command:
        new_elements = [(element - 1) for element in new_elements]
    command = input()
results = [str(element) for element in new_elements]
print(', '.join(results))
