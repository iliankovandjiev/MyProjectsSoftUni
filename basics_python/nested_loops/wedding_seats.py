last_sector = input()
rows_sector = int(input())
odd_seats_in_row = int(input())
even_seats_in_row = odd_seats_in_row + 2
counter = 0
digit_last_sector = ord(last_sector)
total_rows = digit_last_sector - 65
counter_seat = 0
# 65-90
for sectors in range(65, digit_last_sector + 1):
    symbol_sectors = chr(sectors)
    for rows in range(1, (rows_sector + counter_seat) + 1):
        if rows % 2 != 0:
            for seat in range(97, (97 + odd_seats_in_row)):
                symbol_seat = chr(seat)
                counter += 1
                print(f'{symbol_sectors}{rows}{symbol_seat}')
        else:
            for seat in range(97, (97 + even_seats_in_row)):
                symbol_seat = chr(seat)
                counter += 1
                print(f'{symbol_sectors}{rows}{symbol_seat}')
    counter_seat += 1
print(counter)