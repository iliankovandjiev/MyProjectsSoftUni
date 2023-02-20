def add_matrix(comm, indexes):
    if valid_indexes(indexes):
        matrix[indexes[0]][indexes[1]] = matrix[indexes[0]][indexes[1]] + indexes[2]


def subtract_matrix(comm, indexes):
    if valid_indexes(indexes):
        matrix[indexes[0]][indexes[1]] = matrix[indexes[0]][indexes[1]] - indexes[2]


def valid_indexes(indexes):
    if 0 <= indexes[0] < len(matrix) and 0 <= indexes[1] < len(matrix[0]):
        return True
    print("Invalid coordinates")


rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

while True:
    command, *info = [int(x) if x[-1].isdigit() else x for x in input().split(" ")]
    if command == "END":
        break

    elif command == "Add":
        add_matrix(command, info)

    elif command == "Subtract":
        subtract_matrix(command, info)

[print(*row) for row in matrix]