capacity = int(input())
fans = int(input())
sec_a = 0
sec_b = 0
sec_v = 0
sec_g = 0
for i in range (fans):
    sector = input()
    if sector == "A":
        sec_a += 1
    elif sector == 'B':
        sec_b += 1
    elif sector == 'V':
        sec_v += 1
    elif sector == 'G':
        sec_g += 1
total_sec = sec_g + sec_v + sec_b + sec_a
per_sec_a = sec_a / total_sec * 100
per_sec_b = sec_b / total_sec * 100
per_sec_v = sec_v / total_sec * 100
per_sec_g = sec_g / total_sec * 100
per_fen_cap = fans / capacity * 100
print(f'{per_sec_a:.2f}%')
print(f'{per_sec_b:.2f}%')
print(f'{per_sec_v:.2f}%')
print(f'{per_sec_g:.2f}%')
print(f'{per_fen_cap:.2f}%')