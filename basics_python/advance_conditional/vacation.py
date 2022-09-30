budget = float(input())
season = input()
location = ''
place = ''
price = 0
if budget <= 1000:
    location = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        price = 0.65 * budget
    elif season == 'Winter':
        place = 'Morocco'
        price = 0.45 * budget
elif budget <= 3000:
    location = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        price = 0.8 * budget
    elif season == 'Winter':
        place = 'Morocco'
        price = 0.60 * budget
else:
    location = 'Hotel'
    if season == 'Summer':
        place = 'Alaska'
        price = 0.9 * budget
    elif season == 'Winter':
        place = 'Morocco'
        price = 0.9 * budget
print(f'{place} - {location} - {price:.2f}')





