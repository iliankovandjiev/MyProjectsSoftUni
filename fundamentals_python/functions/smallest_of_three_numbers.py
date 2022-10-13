number_one = int(input())
number_two = int(input())
number_three = int(input())


def smallest(a, b, c):
    min_num = min(a, b, c)
    return min_num


print(smallest(number_one, number_two, number_three))
