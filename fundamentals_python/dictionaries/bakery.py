input_line = input().split(' ')
bakery = {}
for index in range(0, len(input_line), 2):
    keys = input_line[index]
    value = input_line[index + 1]
    bakery[keys] = int(value)
print(bakery)
