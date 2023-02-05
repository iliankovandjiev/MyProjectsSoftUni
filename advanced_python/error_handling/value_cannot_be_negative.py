class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    read_number = int(input())
    if read_number < 0:
        raise ValueCannotBeNegative
    