inp_line = input()
steps_counter = 0
diff = 0
while inp_line != 'Going home':
    steps = int(inp_line)
    steps_counter += steps
    if steps_counter >= 10000:
        break
    inp_line = input()
steps = str(inp_line)
if steps == 'Going home':
    steps = int(input())
    steps_counter += steps
    if steps_counter >= 10000:
        diff = steps_counter - 10000
        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
    else:
        diff = 10000 - steps_counter
        print(f'{diff} more steps to reach goal.')
else:
    diff = steps_counter - 10000
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')