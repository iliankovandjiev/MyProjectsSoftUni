percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())
total_calories_of_food = 0
grams_fats = ((percent_fats / 100) * total_calories) / 9
grams_proteins = ((percent_proteins / 100) * total_calories) / 4
grams_carbohydrates = ((percent_carbohydrates / 100) * total_calories) / 4
total_calories_of_food = grams_fats +  grams_proteins + grams_carbohydrates
calories_for_on_gram = total_calories / total_calories_of_food
grams_fats_of_this_recept = calories_for_on_gram * ((100 - percent_water) / 100)
print(f'{grams_fats_of_this_recept:.4f}')