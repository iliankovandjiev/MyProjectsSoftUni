n_number = int(input())
for i in range(n_number):
    string_inp = input()
    for char in range(len(string_inp)):
        pure = string_inp[char]
        if pure == ',' or pure == '.' or pure == '_':
            print(f'{string_inp} is not pure!')
            break
    else:
        print(f'{string_inp} is pure.')
