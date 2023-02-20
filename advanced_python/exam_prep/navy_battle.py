size = int(input())
battlefield = []
submarine_pos = []
take_damage = 0
cruisers_count = 0

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = []
    for col in input():
        line.append(col)
    battlefield.append(line)
    if "S" in battlefield[row]:
        submarine_pos = [row, battlefield[row].index("S")]
        battlefield[row][submarine_pos[1]] = "-"
    if "C" in battlefield[row]:
        cruisers_count += battlefield[row].count("C")

while take_damage < 4 and cruisers_count > 0:
    command = input()
    r = submarine_pos[0] + direction[command][0]
    c = submarine_pos[1] + direction[command][1]

    if battlefield[r][c] == "*":
        submarine_pos = [r, c]
        take_damage += 1
        battlefield[r][c] = "-"
        if take_damage == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            battlefield[r][c] = "S"
            break
    elif battlefield[r][c] == "C":
        submarine_pos = [r, c]
        cruisers_count -= 1
        battlefield[r][c] = "-"
        if cruisers_count == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[r][c] = "S"
            break
    else:
        submarine_pos = [r, c]

[print("".join(row)) for row in battlefield]


