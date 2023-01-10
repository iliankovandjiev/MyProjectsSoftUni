from collections import deque

water_in_l = int(input())
command = input()
people_queue = deque()
while command != 'Start':
    people_queue.append(command)
    command = input()
second_command = input()
while second_command != 'End':
    if second_command.isdigit():
        liters = int(second_command)
        if water_in_l >= liters:
            print(f'{people_queue.popleft()} got water')
            water_in_l -= liters
        else:
            print(f'{people_queue.popleft()} must wait')
    else:
        refill_liters = second_command.replace('refill', '').replace(' ', '')
        liters = int(refill_liters)
        water_in_l += liters
    second_command = input()
print(f"{water_in_l} liters left")
