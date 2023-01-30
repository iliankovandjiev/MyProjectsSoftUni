unique_element = set()

for _ in range(int(input())):
    element = input().split()
    for elem in element:
        unique_element.add(elem)


print(*unique_element, sep="\n")
