number = int(input())
for special_number in range(1111, 10000):
    special_number_str = str(special_number)
    for char in special_number_str:
        char = int(char)
        its_special = True
        if char == 0 or number % char != 0:
            its_special = False
            break
    if its_special:
        print(special_number_str, end=' ')
