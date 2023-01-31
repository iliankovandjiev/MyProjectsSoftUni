matrix = []
total_sum = 0
rows, columns = [int(x) for x in input().split(", ")]

for _ in range(rows):
    matrix_input = list(map(lambda x: int(x), input().split(', ')))
    matrix.append(matrix_input)
    total_sum += sum(matrix_input)

print(total_sum)
print(matrix)