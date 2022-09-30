quantity_of_decorations = int(input())
days = int(input())
budget = 0
total_spirit = 0
days_left = days
ornament_sets_price = 2
ornament_sets_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17
days_passed = 0
while days_left > 0:
    days_passed += 1
    if days_passed % 11 == 0:
        quantity_of_decorations += 2
    if days_passed % 2 == 0:
        budget += ornament_sets_price * quantity_of_decorations
        total_spirit += ornament_sets_points
    if days_passed % 3 == 0:
        budget += tree_skirt_price * quantity_of_decorations + tree_garland_price * quantity_of_decorations
        total_spirit += tree_skirt_points+ tree_garland_points
    if days_passed % 5 == 0:
        budget += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
        if days_passed % 3 == 0:
            total_spirit += 30
    if days_passed % 10 == 0:
        total_spirit -= 20
        budget += tree_lights_price + tree_garland_price + tree_skirt_price
    days_left -= 1
    if days_left == 0 and days_passed % 10 == 0:
        total_spirit -= 30
print(f'Total cost: {budget}')
print(f'Total spirit: {total_spirit}')



