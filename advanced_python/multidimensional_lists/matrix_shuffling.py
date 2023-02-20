def check_valid_index(indexes):
    if set(indexes[:2]).issubset(valid_rows) and set(indexes[2:]).issubset(valid_columns):
        return True

    return False


def snap_command(comm, indexes):
    if check_valid_index(indexes) and comm == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")

    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split(" ")]
matrix = [input().split(" ") for _ in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split(" ")]

    if command == "END":
        break

    snap_command(command, info)
