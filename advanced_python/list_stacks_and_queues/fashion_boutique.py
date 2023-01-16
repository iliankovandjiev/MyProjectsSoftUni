box_of_clothes = [int(c) for c in input().split()]
capacity_of_one_rack = int(input())
left_capacity = capacity_of_one_rack
total_clothes = 0
racks_count = 1

while box_of_clothes:

    current_clothes = box_of_clothes.pop()
    if left_capacity > current_clothes:
        left_capacity -= current_clothes
    elif left_capacity == current_clothes:
        left_capacity = capacity_of_one_rack
        if box_of_clothes:
            racks_count += 1
    else:
        left_capacity = capacity_of_one_rack
        racks_count += 1
        left_capacity -= current_clothes

print(racks_count)