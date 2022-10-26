first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_sequence = []
for first in first_sequence:
    for second in second_sequence:
        if first in second:
            if first not in new_sequence:
                new_sequence.append(first)
print(new_sequence)

