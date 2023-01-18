numbers_input = tuple(float(num) for num in input().split())
nums_and_occurrences = {}

for num in numbers_input:
    if num not in nums_and_occurrences:
        nums_and_occurrences[num] = 0
    nums_and_occurrences[num] += 1

[print(f'{number:.1f} - {int(count)} times') for number, count in nums_and_occurrences.items()]

