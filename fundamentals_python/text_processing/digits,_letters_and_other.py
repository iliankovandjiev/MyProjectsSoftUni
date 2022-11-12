single_string = input()
digits, words, symbols = [], [], []
for symbol in single_string:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        words.append(symbol)
    else:
        symbols.append(symbol)
print(''.join(digits))
print(''.join(words))
print(''.join(symbols))

