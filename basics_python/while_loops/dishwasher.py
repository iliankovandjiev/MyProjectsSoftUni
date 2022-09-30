detergent = int(input())
comm_input = input()
total_detergent = detergent * 750
needed_detergent = 0
detergent_is_finish = False
count = 0
num_plates = 0
num_pot = 0
while comm_input != 'End':
    comm_input = int(comm_input)
    count += 1
    if count % 3 == 0:
        needed_detergent += comm_input * 15
        num_pot += comm_input
    else:
        needed_detergent += comm_input * 5
        num_plates += comm_input
    if needed_detergent > total_detergent:
        detergent_is_finish = True
        break
    comm_input = input()
diff = abs(total_detergent - needed_detergent)
if detergent_is_finish:
    print(f'Not enough detergent, {diff} ml. more necessary!')
else:
    print(f'Detergent was enough!')
    print(f'{num_plates} dishes and {num_pot} pots were washed.')
    print(f'Leftover detergent {diff} ml.')


