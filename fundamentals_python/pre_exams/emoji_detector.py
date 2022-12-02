import re


emojis_dict = {}
text_input = input()
cool_threshold = 1
pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
valid_emoji = re.findall(pattern, text_input)
for emoji in valid_emoji:
    score = 0
    for point in emoji[1]:
        score += ord(point)
    emojis_dict[emoji[1]] = int(score)
for digit in text_input:
    if digit.isdigit():
        cool_threshold *= int(digit)
print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis_dict)} emojis found in the text. The cool ones are:')
for cool_ones in emojis_dict:
    if emojis_dict[cool_ones] >= cool_threshold:
        for emoji in valid_emoji:
            if cool_ones in emoji:
                print(emoji[0]+emoji[1]+emoji[0])
