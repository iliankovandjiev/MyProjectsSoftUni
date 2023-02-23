def create_fun(pos, direc, val):
    r = pos[0] + directions[direc][0]
    c = pos[1] + directions[direc][1]

    if matrix[r][c] == ".":
        matrix[r][c] = val

    position = [r, c]
    return position


def update_fun(pos, direc, val):
    r = pos[0] + directions[direc][0]
    c = pos[1] + directions[direc][1]

    if matrix[r][c].isdigit() or matrix[r][c].isalpha():
        matrix[r][c] = val

    position = [r, c]
    return position


def delete_fun(pos, direc):
    r = pos[0] + directions[direc][0]
    c = pos[1] + directions[direc][1]

    matrix[r][c] = "."

    position = [r, c]
    return position


def read_fun(pos, direc):
    r = pos[0] + directions[direc][0]
    c = pos[1] + directions[direc][1]

    if not matrix[r][c] == ".":
        print(matrix[r][c])

    position = [r, c]
    return position


size = 6
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

position = [int(x) for x in input() if x.isdigit()]

command, *info = input().split(", ")

while command != "Stop":

    if command == "Create":
        direction, value = info
        position = create_fun(position, direction, value)
    elif command == "Update":
        direction, value = info
        position = update_fun(position, direction, value)
    elif command == "Delete":
        direction = info[0]
        position = delete_fun(position, direction)
    elif command == "Read":
        direction = info[0]
        position = read_fun(position, direction)

    command, *info = input().split(", ")

[print(" ".join(mat)) for mat in matrix]