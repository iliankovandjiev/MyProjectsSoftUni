row = int(input())
primary_sum = 0
secondary_sum = 0
primary_diagonal = []
secondary_diagonal = []
n = 0

matrix = [[int(element) for element in input().split(", ")] for _ in range(row)]
for primary in range(row):
    primary_sum += matrix[primary][primary]
    primary_diagonal.append(matrix[primary][primary])

for secondary in range(row - 1, -1, -1):
    secondary_sum += matrix[n][secondary]
    secondary_diagonal.append(matrix[n][secondary])
    n += 1

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")
