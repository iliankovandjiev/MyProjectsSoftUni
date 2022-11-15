text_input = input()
emoticon = []
for index, char in enumerate(text_input):
    if char == ':':
        emoticon.append(f':{text_input[index + 1]}')
print('\n'.join(emoticon))