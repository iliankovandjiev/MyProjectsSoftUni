letter = ''
number_of_floor = int(input())
number_of_rooms = int(input())
for i in range(number_of_floor, 0, -1):
    for y in range(number_of_rooms):
        if i == number_of_floor:
            letter = 'L'
        elif i % 2 == 0:
            letter = 'O'
        else:
            letter = "A"
        print(f'{letter}{i}{y}', end=" ")
    print()