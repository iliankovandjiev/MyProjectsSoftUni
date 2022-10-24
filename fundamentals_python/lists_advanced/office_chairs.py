number_of_room = int(input())
total_chairs = 0
total_visitors = 0
free_chairs = True
for room in range(1, number_of_room + 1):
    chairs, visitors = input().split()
    total_chairs += len(chairs)
    total_visitors += int(visitors)
    if len(chairs) < int(visitors):
        chairs_needed = len(chairs) - int(visitors)
        print(f"{abs(chairs_needed)} more chairs needed in room {room}")
        free_chairs = False
if free_chairs:
    total_free_chairs = total_chairs - total_visitors
    print(f"Game On, {total_free_chairs} free chairs left")