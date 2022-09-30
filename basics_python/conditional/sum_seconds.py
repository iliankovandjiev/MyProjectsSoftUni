time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third
time_min = total_time // 60
time_sec = total_time % 60
if time_sec < 10:
    print(f'{time_min}:0{time_sec}')
else:
    print(f'{time_min}:{time_sec}')
