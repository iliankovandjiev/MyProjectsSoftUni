import math

num_tournament = int(input())
start_points = int(input())
final_point = 0
win = 0
for i in range(num_tournament):
    stage = str(input())
    if stage == 'W':
        final_point += 2000
        win += 1
    elif stage == 'F':
        final_point += 1200
    elif stage == 'SF':
        final_point += 720
average_point = final_point / num_tournament
final_point += start_points
perc_win = win / num_tournament * 100
print(f'Final points: {final_point}')
print(f'Average points: {math.floor(average_point)}')
print(f'{perc_win:.2f}%')

