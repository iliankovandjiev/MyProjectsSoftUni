numbers_of_snowballs = int(input())
best_snowball = 0
best_weight_of_snowball = 0
best_time_needed_for_snowball = 0
best_quality_of_snowball = 0
for i in range(numbers_of_snowballs):
    weight_of_snowball = int(input())
    time_needed_for_snowball = int(input())
    quality_of_snowball = int(input())
    value_of_snowball = (weight_of_snowball / time_needed_for_snowball) ** quality_of_snowball
    if best_snowball < value_of_snowball:
        best_snowball = value_of_snowball
        best_weight_of_snowball = weight_of_snowball
        best_time_needed_for_snowball = time_needed_for_snowball
        best_quality_of_snowball = quality_of_snowball


print(f'{best_weight_of_snowball} : {best_time_needed_for_snowball} = {best_snowball:.0f} ({best_quality_of_snowball})')