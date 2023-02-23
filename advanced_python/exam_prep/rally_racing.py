size = int(input())
racing_number = input()
car_pos = [0, 0]
track = []
kilometers = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for row in range(size):
    track.append(input().split(" "))


while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    r = car_pos[0] + directions[command][0]
    c = car_pos[1] + directions[command][1]

    if track[r][c] == "T":
        track[r][c] = "."
        kilometers += 30
        for row in range(len(track)):
            if "T" in track[row]:
                r, c = row, track[row].index("T")
                track[r][c] = "."
                car_pos[0] = r
                car_pos[1] = c

    elif track[r][c] == "F":
        kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        track[r][c] = "."
        car_pos[0] = r
        car_pos[1] = c
        break

    else:
        kilometers += 10
        car_pos[0] = r
        car_pos[1] = c

track[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {kilometers} km.")
[print(''.join(row)) for row in track]
