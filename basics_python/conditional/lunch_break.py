import math

name_serial = str(input())
duration_serial = int(input())
duration_break = int(input())
lunch_time = duration_break / 8
break_time = duration_break / 4
time_left = duration_break - lunch_time - break_time
if time_left >= duration_serial:
    time_left_after_serial = time_left - duration_serial
    print(f'You have enough time to watch {name_serial} and left with {math.ceil(time_left_after_serial)} minutes free time.')
else:
    time_needed = duration_serial - time_left
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(time_needed)} more minutes.")
