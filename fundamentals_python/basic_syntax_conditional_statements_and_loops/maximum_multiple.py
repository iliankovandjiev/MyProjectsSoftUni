divisor = int(input())
boundary = int(input())
number_found = boundary
while boundary % divisor != 0:
    boundary -= 1
    number_found = boundary
print(number_found)
