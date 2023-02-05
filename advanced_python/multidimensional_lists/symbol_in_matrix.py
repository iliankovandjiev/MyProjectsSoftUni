number_of_square_matrix = int(input())
matrix = []
searched_symbol_found = False

for _ in range(number_of_square_matrix):
    matrix.append(list(input()))

searched_symbol = input()

for row in range(number_of_square_matrix):
    if searched_symbol_found:
        break
    for column in range(number_of_square_matrix):
        if searched_symbol == matrix[row][column]:
            print(f"({row}, {column})")
            searched_symbol_found = True


if not searched_symbol_found:
    print(f'{searched_symbol} does not occur in the matrix')
