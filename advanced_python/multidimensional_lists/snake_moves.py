from collections import deque

rows, columns = [int(x) for x in input().split(" ")]
word = input()

copy_word = deque(word)

for row in range(rows):
    while len(copy_word) < columns:
        copy_word.extend(word)

    if row % 2 == 0:
        print(*[copy_word.popleft() for _ in range(columns)], sep="")
    else:
        print(*[copy_word.popleft() for _ in range(columns)][::-1], sep="")