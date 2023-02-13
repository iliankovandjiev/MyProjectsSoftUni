rows, columns = input().split(" ")
matrix = [[el for el in input().split(" ")] for _ in range(int(rows))]
num_of_squares = 0

for row in range(0, int(rows) - 1):
    for column in range(0, int(columns) - 1):
        symbol_1 = matrix[row][column]
        symbol_2 = matrix[row][column + 1]
        symbol_3 = matrix[row + 1][column]
        symbol_4 = matrix[row + 1][column + 1]

        if symbol_1 == symbol_2 and symbol_3 == symbol_4 and symbol_1 == symbol_3:
            num_of_squares += 1

print(num_of_squares)