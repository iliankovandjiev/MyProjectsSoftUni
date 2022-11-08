info_input = input().split('-')
contact_dict = {}
while True:
    if not len(info_input) > 1:
        break
    contact_dict[info_input[0]] = info_input[1]
    info_input = input().split('-')
for name in range(int(info_input[0])):
    names = input()
    if names in contact_dict:
        print(f"{names} -> {contact_dict[names]}")
    else:
        print(f"Contact {names} does not exist.")

