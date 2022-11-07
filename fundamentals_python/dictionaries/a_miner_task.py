resource_dict = {}
while True:
    command1 = input()
    if command1 == 'stop':
        break
    command2 = int(input())
    if command1 not in resource_dict:
        resource_dict[command1] = 0
    resource_dict[command1] += command2
for resource, quantity in resource_dict.items():
    print(f"{resource} -> {quantity}")

