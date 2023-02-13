row = int(input())
primary_sum = 0
secondary_sum = 0
matrix = [[int(element) for element in input().split(" ")] for _ in range(row)]
n = 0

for primary in range(row):
    primary_sum += matrix[primary][primary]

for secondary in range(row - 1, -1, -1):
    secondary_sum += matrix[n][secondary]
    n += 1

absolut_difference = abs(primary_sum - secondary_sum)
print(absolut_difference)