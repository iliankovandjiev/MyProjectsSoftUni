people_waiting = int(input())
current_state = input()
final_state = ''
for index in range(0, len(current_state), 2):
    cabin = int(current_state[index])
    while cabin != 4:
        if people_waiting > 0:
            people_waiting -= 1
        else:
            break
        cabin += 1
    final_state += str(cabin) + ' '
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(final_state)
elif people_waiting == 0 and cabin == 4:
    print(final_state)
else:
    print('The lift has empty spots!')
    print(final_state)
