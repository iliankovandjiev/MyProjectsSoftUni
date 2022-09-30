n_stars = int(input())
for row in range(n_stars):
    for column in range(row + 1):
        print('*', end="")
    print('')
for row in range(n_stars):
    for column in range(row, n_stars - 1):
        print('*', end="")
    print('')