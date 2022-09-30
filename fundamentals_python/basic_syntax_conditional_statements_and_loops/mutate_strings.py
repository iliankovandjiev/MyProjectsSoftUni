first_string = input()
second_string = input()
new_word = first_string
for char in range(len(first_string)):
    if first_string[char] != second_string[char]:
        letter = list(new_word)
        letter[char] = second_string[char]
        new_word = ''.join(letter)
        print(new_word)

