
longest_intersection = []

for _ in range(int(input())):
    first_range, second_range = (num.split(",") for num in input().split('-'))
    intersection_one = set(range(int(first_range[0]), int(first_range[1]) + 1))
    intersection_two = set(range(int(second_range[0]), int(second_range[1]) + 1))
    intersection = intersection_one.intersection(intersection_two)
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection
print(f'Longest intersection is [{", ".join(str(el) for el in longest_intersection)}] '
      f'with length {len(longest_intersection)}')
