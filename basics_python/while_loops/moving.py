width = int(input())
lenght = int(input())
height = int(input())
input_comand = input()
space_left = width * lenght * height
no_more_space = False
diff = 0
while input_comand != 'Done':
    num_box = int(input_comand)
    space_left -= num_box
    if space_left <= 0:
        no_more_space = True
        break
    input_comand = input()
if no_more_space:
    print(f'No more free space! You need {abs(space_left)} Cubic meters more.')
else:
    print(f'{space_left} Cubic meters left.')