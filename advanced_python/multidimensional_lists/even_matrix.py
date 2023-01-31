rows_of_matrix = int(input())
new_matrix = []

for _ in range(rows_of_matrix):
    row = [int(elem) for elem in input().split(", ") if int(elem) % 2 == 0]
    new_matrix.append(row)


print(new_matrix)
