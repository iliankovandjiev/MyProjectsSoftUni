string_of_banned_words = input().split(', ')
text_input = input()
for banned_word in string_of_banned_words:
    text_input = text_input.replace(banned_word, '*' * len(banned_word))
print(text_input)