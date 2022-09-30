tipe_of_projection = str(input())
rows = int(input())
columns = int(input())
volume_cinema = rows * columns
price_ticket = 0
if tipe_of_projection == 'Premiere':
    price_ticket = volume_cinema * 12
elif tipe_of_projection == 'Normal':
    price_ticket = volume_cinema * 7.5
elif tipe_of_projection == 'Discount':
    price_ticket = volume_cinema * 5
print(f'{price_ticket:.2f} leva')