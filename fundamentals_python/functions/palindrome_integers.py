list_of_positive_integers = input().split(", ")
for num in list_of_positive_integers:
    if num[:] == num[::-1]:
        print(True)
    else:
        print(False)