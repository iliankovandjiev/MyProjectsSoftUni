month = str(input())
number_of_sleep = int(input())
studio = 0
apartment = 0
price = 0
if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if number_of_sleep > 14:
        studio = studio * 0.70
        apartment = apartment * 0.9
    elif number_of_sleep > 7:
        studio = studio * 0.95
elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    if number_of_sleep > 14:
        studio = studio * 0.80
        apartment = apartment * 0.9
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if number_of_sleep > 14:
        apartment = apartment * 0.9
print(f'Apartment: {(number_of_sleep * apartment):.2f} lv.')
print(f'Studio: {(number_of_sleep * studio):.2f} lv.')

