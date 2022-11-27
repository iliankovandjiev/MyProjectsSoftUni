import re

text_string = input()
pattern = r'(\#|\|)([A-Za-z ]+)\1([0-9]{2}\/[][0-9]{2}\/[][0-9]{2})\1([1-9][0-9]?[0-9]?[0-9]?[0-9]?|10000)\1'
sum_of_calories = 0
matches = re.findall(pattern, text_string)
for i in range(len(matches)):
    sum_of_calories += int(matches[i][3])
days = sum_of_calories // 2000
print(f'You have food to last you for: {days} days!')
for food in range(len(matches)):
    item_name = matches[food][1]
    expiration_date = matches[food][2]
    calories = matches[food][3]
    print(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
