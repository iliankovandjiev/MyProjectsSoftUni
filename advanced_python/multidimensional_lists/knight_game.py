size_of_board = int(input())
matrix = [list(input()) for _ in range(size_of_board)]

positions = {
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (-1, -2),
    (2, -1),
    (2, 1),
    (1, 2),
    (1, -2),
}

removed_knights = 0

while True:
    attacks = 0
    knight_position = []

    for row in range(size_of_board):
        for col in range(size_of_board):
            if matrix[row][col] == "K":
                current_attack = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size_of_board and 0 <= pos_col < size_of_board:

                        if matrix[pos_row][pos_col] == "K":
                            current_attack += 1

                if attacks < current_attack:
                    knight_position = [row, col]
                    attacks = current_attack

    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = "O"
        removed_knights += 1
    else:
        break

print(removed_knights)