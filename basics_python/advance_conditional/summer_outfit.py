celcius = int(input())
day_time = str(input())
outfit = ''
shoes = ''
if 10 <= celcius <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < celcius <= 24:
    if day_time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif celcius >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")