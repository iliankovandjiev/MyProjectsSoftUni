number_one = int(input())
number_two = int(input())
max_symbols = int(input())
total_pass = 0
symbol_a = 35
symbol_b = 64
for symbol_x in range(1, number_one + 1):
    for symbol_y in range(1, number_two + 1):
        if total_pass >= max_symbols:
            break
        if symbol_a <= 55:
            chr_symbol_a = chr(symbol_a)
        else:
            symbol_a = 35
            chr_symbol_a = chr(symbol_a)
        if symbol_b <= 96:
            chr_symbol_b = chr(symbol_b)
        else:
            symbol_b = 64
            chr_symbol_b = chr(symbol_b)
        print(f'{chr_symbol_a}{chr_symbol_b}{symbol_x}{symbol_y}{chr_symbol_b}{chr_symbol_a}', end='|')
        total_pass += 1
        symbol_a += 1
        symbol_b += 1

