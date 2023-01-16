from collections import deque

quantity_of_food = int(input())
food_queue = deque([int(f) for f in input().split()])
order_complete = True

print(max(food_queue))

for order in food_queue.copy():
    if quantity_of_food >= order:
        quantity_of_food -= order
        food_queue.popleft()
    else:
        print(f"Orders left: {' '.join([str(o) for o in food_queue])}")
        order_complete = False
        break

if order_complete:
    print('Orders complete')





