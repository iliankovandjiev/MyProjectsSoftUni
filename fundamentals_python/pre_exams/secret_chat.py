concealed_message = input()
strings_with_instructions = input()
while strings_with_instructions != 'Reveal':
    strings_with_instructions = strings_with_instructions.split(':|:')
    if strings_with_instructions[0] == 'InsertSpace':
        index = int(strings_with_instructions[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif strings_with_instructions[0] == 'Reverse':
        substring = strings_with_instructions[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            new_string = substring[::-1]
            concealed_message = concealed_message + new_string
            print(concealed_message)
        else:
            print('error')
    elif strings_with_instructions[0] == 'ChangeAll':
        substring = strings_with_instructions[1]
        replacement = strings_with_instructions[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    strings_with_instructions = input()

print(f"You have a new text message: {concealed_message}")