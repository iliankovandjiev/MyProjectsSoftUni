import math

santa_claus_left_day = int(input())
left_food = int(input())
food_day_deer_first = float(input())
food_day_deer_second = float(input())
food_day_deer_third = float(input())
needed_food_for_deer_one = santa_claus_left_day * food_day_deer_first
needed_food_for_deer_two = santa_claus_left_day * food_day_deer_second
needed_food_for_deer_three = santa_claus_left_day * food_day_deer_third
total_needed_food = needed_food_for_deer_one + needed_food_for_deer_two + needed_food_for_deer_three
diff = abs(left_food - total_needed_food)
if left_food >= total_needed_food:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')