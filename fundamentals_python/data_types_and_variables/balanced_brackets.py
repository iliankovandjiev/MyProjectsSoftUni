number_of_lines = int(input())
bracket_is_open = False
bracket_is_close = False
expresion_is = False
open_counter = 0
close_counter = 0
for i in range(number_of_lines):
    line_input = input()
    if bracket_is_open and line_input == '(':
        expresion_is = True
    if line_input == ')':
        close_counter += 1
    if line_input == '(':
        bracket_is_open = True
        open_counter += 1
    if line_input == ')' and bracket_is_open:
        bracket_is_close = True
        close_counter += 1
        open_counter += 1
    if bracket_is_open and bracket_is_close:
        bracket_is_open = False
        bracket_is_close = False
if open_counter == close_counter:
    print("BALANCED")
else:
    print('UNBALANCED')

