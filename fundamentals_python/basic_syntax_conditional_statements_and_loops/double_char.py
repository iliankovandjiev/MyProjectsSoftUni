string_input = input()
while string_input != 'End':
    new_word = ''
    if string_input != 'SoftUni':
        for char in range(len(string_input)):
            new_letter = string_input[char]
            new_word += 2 * new_letter
        print(new_word)
    string_input = input()