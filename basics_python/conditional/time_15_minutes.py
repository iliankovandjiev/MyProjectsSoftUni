hour_time = int(input())
minute_time = int(input())
minute_result = minute_time + 15
if minute_result >= 60:
    minute_result = minute_result - 60
    hour_result = hour_time + 1
else:
    minute_result = minute_result
    hour_result = hour_time
if hour_result > 23:
    hour_result = hour_result - 24
if minute_result < 10:
    print(f'{hour_result}:0{minute_result}')
else:
    print(f'{hour_result}:{minute_result}')

