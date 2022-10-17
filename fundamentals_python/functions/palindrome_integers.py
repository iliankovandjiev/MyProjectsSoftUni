def positive(number):
    for num in number:
        if num[:] == num[::-1]:
            print("True")
        else:
            print("False")


list_of_positive_integers = input().split(", ")
positive(list_of_positive_integers)
