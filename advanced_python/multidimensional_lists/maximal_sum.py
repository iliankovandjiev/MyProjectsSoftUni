import sys


rows, columns = input().split(" ")
matrix = [[int(el) for el in input().split(" ")] for _ in range(int(rows))]

total_sum = -sys.maxsize


for row in range(int(rows) - 2):
    for column in range(int(columns) - 2):
        first_row = matrix[row][column:column + 3]
        second_row = matrix[row + 1][column:column + 3]
        third_row = matrix[row + 2][column:column + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > total_sum:
            total_sum = current_sum
            final_matrix = []
            final_matrix.append(first_row)
            final_matrix.append(second_row)
            final_matrix.append(third_row)


print(f'Sum = {total_sum}')
[print(*final_matrix[row]) for row in range(3)]
