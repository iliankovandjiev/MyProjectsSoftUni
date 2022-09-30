season = input()
group_type = input()
num_student = int(input())
num_night = int(input())
price_night = 0
sports = ''
if group_type == 'boys' or group_type == 'girls':
    if season == 'Winter':
        price_night = 9.6 * num_night * num_student
        if group_type == 'boys':
            sports = 'Judo'
        else:
            sports = 'Gymnastics'
    elif season == "Spring":
        price_night = 7.2 * num_night * num_student
        if group_type == 'boys':
            sports = 'Tennis'
        else:
            sports = 'Athletics'
    elif season == "Summer":
        price_night = 15 * num_night * num_student
        if group_type == 'boys':
            sports = 'Football'
        else:
            sports = 'Volleyball'
elif group_type == 'mixed':
    if season == 'Winter':
        price_night = 10 * num_night * num_student
        sports = 'Ski'
    elif season == "Spring":
        price_night = 9.5 * num_night * num_student
        sports = 'Cycling'
    elif season == "Summer":
        price_night = 20 * num_night * num_student
        sports = 'Swimming'
if num_student < 10:
    price_night = price_night
elif 10 <= num_student < 20:
    price_night *= 0.95
elif 20 <= num_student < 50:
    price_night *= 0.85
else:
    price_night *= 0.5
print(f'{sports} {price_night:.2f} lv.')

