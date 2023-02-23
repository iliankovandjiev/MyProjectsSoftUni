n, m = input().split(" ")
touched_opponents = 0
moves = 0
playground = []
position = []
player_counter = 0

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row in range(int(n)):
    playground.append(input().split(" "))
    if "B" in playground[row]:
        position = row, playground[row].index("B")
        playground[position[0]][position[1]] = "-"
    if "P" in playground[row]:
        player_counter += playground[row].count("P")

while True:

    command = input()
    if command == "Finish":
        break
    if player_counter == 0:
        break

    r = position[0] + direction[command][0]
    c = position[1] + direction[command][1]

    if 0 <= r < int(n) and 0 <= c < int(m):
        if playground[r][c] != 'O':
            position = [r, c]
            moves += 1
            if playground[r][c] == 'P':
                playground[r][c] = "-"
                touched_opponents += 1
                player_counter -= 1

playground[position[0]][position[1]] = "B"

print(f'Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}')
