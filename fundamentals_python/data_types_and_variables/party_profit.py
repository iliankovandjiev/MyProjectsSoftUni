import math

group_size = int(input())
days = int(input())
companions_count = group_size
coins = 0
for day_count in range(1, days + 1):
    if day_count % 10 == 0:
        companions_count -= 2
    if day_count % 15 == 0:
        companions_count += 5
    coins += 50
    coins -= companions_count * 2
    if day_count % 3 == 0:
        coins -= companions_count * 3
    if day_count % 5 == 0:
        coins += companions_count * 20
        if day_count % 3 == 0:
            coins -= companions_count * 2
print(f"{companions_count} companions received {math.floor(coins / companions_count)} coins each.")