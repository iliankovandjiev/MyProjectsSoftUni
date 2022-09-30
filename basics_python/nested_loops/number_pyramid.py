number = int(input())
counter = 1
its_printed = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            its_printed = True
            break
    print()
    if its_printed:
        break

