from collections import deque

petrol_in_tank = 0
petrol_pumps = int(input())
pumps_deque = deque([int(x) for x in input().split()] for _ in range(petrol_pumps))
copy_of_pumps_deque = pumps_deque.copy()
counter = 0


while copy_of_pumps_deque:
    petrol, distance = copy_of_pumps_deque.popleft()

    petrol_in_tank += petrol

    if petrol_in_tank < distance:
        pumps_deque.rotate(-1)
        copy_of_pumps_deque = pumps_deque.copy()
        counter += 1
        petrol_in_tank = 0
    else:
        petrol_in_tank -= distance

print(counter)