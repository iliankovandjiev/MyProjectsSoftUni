dim_cake_1 = int(input())
dim_cake_2 = int(input())
total_cake = dim_cake_1 * dim_cake_2
total_parts = 0
cake_is_over = False
while total_cake >= total_parts:
    cake_parts = input()
    if cake_parts == "STOP":
        cake_is_over = True
        break
    cake_parts = int(cake_parts)
    total_parts += cake_parts
diff = abs(total_cake - total_parts)
if cake_is_over:
    if total_parts >= total_cake:
        print(f'No more cake left! You need {diff} pieces more.')
    else:
        print(f'{diff} pieces are left.')

elif total_parts >= total_cake:
    print(f'No more cake left! You need {diff} pieces more.')
else:
    print(f'{diff} pieces are left.')
