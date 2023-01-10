from collections import deque

names_input = deque(input().split(' '))
toss_number = int(input())

while len(names_input) > 1:
    index = toss_number - 1
    while index >= len(names_input):
        index -= len(names_input)
    print(f"Removed {names_input[index]}")
    names_input.remove(names_input[index])
    index_to_rotate = len(names_input) - index
    names_input.rotate(index_to_rotate)

print(f"Last is {names_input[0]}")