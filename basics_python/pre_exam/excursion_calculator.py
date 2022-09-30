numbers_of_people = int(input())
season = input()
price_per_person = 0
total_price = 0
if season == 'spring':
    if numbers_of_people <= 5:
        price_per_person = 50
    else:
        price_per_person = 48
if season == 'summer':
    if numbers_of_people <= 5:
        price_per_person = 48.5
    else:
        price_per_person = 45
    price_per_person *= 0.85
if season == 'autumn':
    if numbers_of_people <= 5:
        price_per_person = 60
    else:
        price_per_person = 49.5
if season == 'winter':
    if numbers_of_people <= 5:
        price_per_person = 86
    else:
        price_per_person = 85
    price_per_person *= 1.08
total_price = price_per_person * numbers_of_people
print(f'{total_price:.2f} leva.')