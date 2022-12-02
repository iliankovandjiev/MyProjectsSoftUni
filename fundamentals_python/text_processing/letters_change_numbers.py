import re
sequence_of_strings = input()
sequence_of_strings = re.sub(' +', ' ', sequence_of_strings).split()
total_sum = 0
for string in sequence_of_strings:
    number_to_play = ''
    if string[0].isupper():
        first_number = (ord(string[0]) - 64)
        for num in string:
            if num.isdigit():
                number_to_play += num
        number_to_play = int(number_to_play)
        first_operation = (number_to_play / first_number)
        if string[-1].isupper():
            second_number = (ord(string[-1]) - 64)
            total_sum += (first_operation - second_number)
        else:
            second_number = (ord(string[-1]) - 96)
            total_sum += (first_operation + second_number)
    else:
        first_number = (ord(string[0]) - 96)
        for num in string:
            if num.isdigit():
                number_to_play += num
        number_to_play = int(number_to_play)
        first_operation = (number_to_play * first_number)
        if string[-1].isupper():
            second_number = (ord(string[-1]) - 64)
            total_sum += (first_operation - second_number)
        else:
            second_number = (ord(string[-1]) - 96)
            total_sum += (first_operation + second_number)
print(f'{total_sum:.2f}')

