day_rest = int(input())
room_type = str(input())
review = str(input())
nights = day_rest - 1
price_room = 0
total_price = 0
if room_type == "room for one person":
    price_room = 18
    total_price = price_room * nights
    if review == "positive":
        total_price = total_price * 1.25
    else:
        total_price = total_price * 0.9
elif room_type == 'apartment':
    price_room = 25
    total_price = price_room * nights
    if nights < 10:
        total_price = total_price * 0.70
    elif nights <= 15:
        total_price = total_price * 0.65
    else:
        total_price = total_price * 0.5
    if review == "positive":
        total_price = total_price * 1.25
    else:
        total_price = total_price * 0.9
elif room_type == 'president apartment':
    price_room = 35
    total_price = price_room * nights
    if nights < 10:
        total_price = total_price * 0.90
    elif nights <= 15:
        total_price = total_price * 0.85
    else:
        total_price = total_price * 0.80
    if review == "positive":
        total_price = total_price * 1.25
    else:
        total_price = total_price * 0.9
print(f'{total_price:.2f}')