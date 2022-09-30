import math

world_record = float(input())
distance = float(input())
time_for_m = float(input())
resistance = math.floor(distance / 15) * 12.5
time_ivan = distance * time_for_m + resistance
difference = abs(world_record - time_ivan)
if time_ivan < world_record:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')