def move_func(direction, steps):
    row_dir = my_pos[0] + (directions[direction][0] * steps)
    col_dir = my_pos[1] + (directions[direction][1] * steps)

    if not (0 <= row_dir < size and 0 <= col_dir < size):
        return my_pos

    elif matrix[row_dir][col_dir] == "x":
        return my_pos

    return [row_dir, col_dir]


def shoot_func(direction):
    shoot_dir_row = my_pos[0] + directions[direction][0]
    shoot_dir_col = my_pos[1] + directions[direction][1]

    while 0 <= shoot_dir_row < size and 0 <= shoot_dir_col < size:
        if matrix[shoot_dir_row][shoot_dir_col] == "x":
            matrix[shoot_dir_row][shoot_dir_col] = "."
            return [shoot_dir_row, shoot_dir_col]
        else:
            shoot_dir_row += directions[direction][0]
            shoot_dir_col += directions[direction][1]


size = 5
matrix = []
my_pos = []
targets = 0
targets_down = 0
targets_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        my_pos = [row, matrix[row].index("A")]
        matrix[row][my_pos[1]] = "."

    if "x" in matrix[row]:
        targets += matrix[row].count("x")

for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        targets_down_pos = shoot_func(command[1])
        if targets_down_pos:
            targets_pos.append(targets_down_pos)
            targets_down += 1

        if targets_down == targets:
            print(f"Training completed! All {targets_down} targets hit.")
            break

    elif command[0] == "move":
        my_pos = move_func(command[1], int(command[2]))

else:
    print(f"Training not completed! {targets - targets_down} targets left.")

print(*targets_pos, sep="\n")
