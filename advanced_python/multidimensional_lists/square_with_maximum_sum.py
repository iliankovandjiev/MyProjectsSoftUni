rows, columns = input().split(", ")
matrix = []
biggest_sum = 0
found_submatrix = []

for _ in range(int(rows)):
    row = [int(el) for el in input().split(', ')]
    matrix.append(row)

for i in range(int(rows) - 1):
    for j in range(int(columns) - 1):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            found_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

for i in range(2):
    for j in range(2):
        print(found_submatrix[i][j], end=' ')
    print()
print(biggest_sum)