first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0
combination_is_found = False
for i in range(first_number, second_number + 1):
    for y in range(first_number, second_number + 1):
        combination += 1
        if i + y == magic_number:
            combination_is_found = True
            break
        if combination_is_found:
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combination} ({i} + {y} = {magic_number})")
else:
    print(f'{combination} combinations - neither equals {magic_number}')