time_of_exam = int(input())
minute_of_exam = int(input())
time_of_arrive = int(input())
minute_of_arrive = int(input())
hour_of_exam = time_of_exam * 60 + minute_of_exam
hour_of_arrive = time_of_arrive * 60 + minute_of_arrive
if hour_of_arrive <= hour_of_exam <= hour_of_arrive + 30:
    print('On time')
    if hour_of_exam != hour_of_arrive:
        print(f'{hour_of_exam - hour_of_arrive} minutes before the start')
elif hour_of_exam < hour_of_arrive:
    print('Late')
    if hour_of_arrive - hour_of_exam < 60:
        print(f'{hour_of_arrive - hour_of_exam} minutes after the start')
    else:
        time_hour = (hour_of_arrive - hour_of_exam) // 60
        time_minute = (hour_of_arrive - hour_of_exam) % 60
        if time_minute > 9:
            print(f'{time_hour}:{time_minute} hours after the start')
        else:
            print(f'{time_hour}:0{time_minute} hours after the start')
else:
    print('Early')
    if hour_of_exam - hour_of_arrive < 60:
        print(f'{hour_of_exam - hour_of_arrive} minutes before the start')
    else:
        time_hour = (hour_of_exam - hour_of_arrive) // 60
        time_minute = (hour_of_exam - hour_of_arrive) % 60
        if time_minute > 9:
            print(f'{time_hour}:{time_minute} hours before the start')
        else:
            print(f'{time_hour}:0{time_minute} hours before the start')

