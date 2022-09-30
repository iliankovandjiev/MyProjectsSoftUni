word = input()
reverse_word = ''
for x in range(len(word) - 1, -1, -1):
    reverse_word += word[x]
print(reverse_word)
