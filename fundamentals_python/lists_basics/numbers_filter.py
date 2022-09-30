number_of_lines = int(input())
lst_of_number = []
new_lst = []
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'
for i in range(number_of_lines):
    new_number = int(input())
    lst_of_number.append(new_number)
command_input = input()
for current_number in lst_of_number:
    if (
        (command_input == COMMAND_EVEN and current_number % 2 == 0) or
        (command_input == COMMAND_ODD and current_number % 2 != 0) or
        (command_input == COMMAND_NEGATIVE and current_number < 0) or
        (command_input == COMMAND_POSITIVE and current_number >= 0)
    ):
        new_lst.append(current_number)
print(new_lst)
