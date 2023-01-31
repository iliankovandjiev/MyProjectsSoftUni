rows, columns = input().split(', ')
new_matrix = []

for _ in range(int(rows)):
    matrix = [int(el) for el in input().split()]
    new_matrix.append(matrix)

for i in range(int(columns)):
    sum_matrix = 0
    for j in range(int(rows)):
        sum_matrix += new_matrix[j][i]
    print(sum_matrix)
