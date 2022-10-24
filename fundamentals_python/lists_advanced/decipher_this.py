secret_massage = input().split()
new_massage = []
for letter in secret_massage:
    num_to_letter = ''
    word = []
    for char in letter:
        digit = char.isdigit()
        if digit:
            num_to_letter += ''.join(char)
    letter = list(filter(lambda i: i not in num_to_letter, letter))
    num_letter = int(num_to_letter)
    first_letter = chr(num_letter)
    word.append(first_letter)
    letter[0], letter[-1] = letter[-1], letter[0]
    word.append(''.join(letter))
    new_massage.append(''.join(word))
print(' '.join(new_massage))
