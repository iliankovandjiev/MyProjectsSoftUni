import re

text_string = input()
pattern = r'(\@|\#)([A-Za-z][A-Za-z][A-Za-z]+)\1{2}([A-Za-z][A-Za-z][A-Za-z]+)\1'
count_of_matches = 0
mirror_word = []
word_pairs = re.findall(pattern, text_string)
found_mirror_word = False
for word in word_pairs:
    if word[1] == word[2][::-1]:
        count_of_matches += 1
        mirror_word.append(f'{word[1]} <=> {word[2]}')
        found_mirror_word = True
    else:
        count_of_matches += 1
if count_of_matches == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{count_of_matches} word pairs found!")
    if not found_mirror_word:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_word))