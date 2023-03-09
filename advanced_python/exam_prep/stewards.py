from collections import deque

rotation_count = 0
found_seat = 0
seat_match = []
seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

while rotation_count < 10 and found_seat < 3:

    rotation_count += 1
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    ascii_character = chr(first_number + second_number)
    first_combination = str(first_number) + ascii_character
    second_combination = str(second_number) + ascii_character

    if first_combination in seats:
        seat_match.append(first_combination)
        seats.remove(first_combination)
        found_seat += 1

    elif second_combination in seats:
        seat_match.append(second_combination)
        seats.remove(second_combination)
        found_seat += 1

    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(seat_match)}")
print(f"Rotations count: {rotation_count}")

