size = int(input())
matrix = []
bags_of_tea = 0
alice_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while bags_of_tea < 10:
    direction = input()

    new_row = alice_pos[0] + directions[direction][0]
    new_col = alice_pos[1] + directions[direction][1]

    if not (0 <= new_row < size and 0 <= new_col < size):
        break

    if matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break

    if matrix[new_row][new_col].isdigit():
        bags_of_tea += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = "*"
        alice_pos = [new_row, new_col]
    else:
        matrix[new_row][new_col] = "*"
        alice_pos = [new_row, new_col]

if bags_of_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]
