import re

string_input = input()
list_of_numbers = []
while string_input:
    pattern = r'\d+'
    extracted_numbers = re.findall(pattern, string_input)
    for num in extracted_numbers:
        if num:
            list_of_numbers.append(num)
    string_input = input()
print(' '.join(list_of_numbers))