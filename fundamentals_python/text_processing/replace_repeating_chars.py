string_input = input()
new_string = ''
for index in range(0, len(string_input) - 1):
    if string_input[index] != string_input[index + 1]:
        new_string += string_input[index]
    if index == int(len(string_input) - 2):
        new_string += string_input[index + 1]
print(new_string)
