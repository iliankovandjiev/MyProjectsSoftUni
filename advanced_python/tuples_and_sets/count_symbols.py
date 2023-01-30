text_dict = {}

for symbol in input():
    if symbol not in text_dict.keys():
        text_dict[symbol] = 0
    text_dict[symbol] += 1

for letter, times in sorted(text_dict.items()):
    print(f'{letter}: {times} time/s')

