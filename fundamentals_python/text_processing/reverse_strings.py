while True:
    word_input = input()
    if word_input == 'end':
        break
    reversed_word = word_input[::-1]
    print(f'{word_input} = {reversed_word}')