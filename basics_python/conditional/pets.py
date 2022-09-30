import math

days = int(input())
food = int(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input())
food_needed = days * (food_dog + food_cat + food_turtle / 1000)
abs_food = abs(food - food_needed)
if food_needed <= food:
    print(f'{math.floor(abs_food)} kilos of food left.')
else:
    print(f'{math.ceil(abs_food)} more kilos of food are needed.')