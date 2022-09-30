import math

non_work_day = int(input())
work_day = 365 - non_work_day
play_time = non_work_day * 127 + work_day * 63
diff_norm = 30000 - play_time
abs_diff = abs(diff_norm)
time_h_left = (math.ceil(abs_diff // 60))
time_m_left = (math.ceil(abs_diff % 60))

if diff_norm >= 0:
    print('Tom sleeps well')
    print(f'{time_h_left} hours and {time_m_left} minutes less for play')
else:
    print('Tom will run away')
    print(f'{time_h_left} hours and {time_m_left} minutes more for play')


