r, c = input().split(" ")

for x in range(int(r)):
    for y in range(int(c)):
        first_letter = chr(97 + x)
        second_letter = chr(97 + x + y)
        third_letter = first_letter
        print(first_letter + second_letter + third_letter, end=" ")
    print()