odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    name = 0
    for letter in input():
        name += ord(letter)

    if int(name / i) % 2 == 0:
        even_set.add(int(name / i))
    else:
        odd_set.add(int(name / i))

if sum(odd_set) == sum(even_set):
    value = odd_set.union(even_set)
    print(*value, sep=", ")
elif sum(odd_set) > sum(even_set):
    value = odd_set.difference(even_set)
    print(*value, sep=", ")
else:
    value = odd_set.symmetric_difference(even_set)
    print(*value, sep=", ")