number_of_square_matrix = int(input())
matrix = []
sum_of_diagonals = 0

for _ in range(number_of_square_matrix):
    row_of_matrix = [int(el) for el in input().split()]
    matrix.append(row_of_matrix)

for i in range(number_of_square_matrix):
    sum_of_diagonals += matrix[i][i]

print(sum_of_diagonals)