
guests_regular = set()
guests_vip = set()

for _ in range(int(input())):
    reservation_code = input()
    if reservation_code[0].isdigit():
        guests_vip.add(reservation_code)
    else:
        guests_regular.add(reservation_code)

while True:
    command = input()
    if command == "END":
        break
    if command[0].isdigit():
        guests_vip.remove(command)
    else:
        guests_regular.remove(command)
print(len(guests_vip) + len(guests_regular))
if guests_vip:
    print('\n'.join(sorted(guests_vip)))
if guests_regular:
    print('\n'.join(sorted(guests_regular)))