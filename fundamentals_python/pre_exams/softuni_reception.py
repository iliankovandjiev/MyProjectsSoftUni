first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())
student_per_hour = first_employee + second_employee + third_employee
counter_hours = 0
while student_count > 0:
    counter_hours += 1
    student_count -= student_per_hour
    if counter_hours % 4 == 0:
        student_count += student_per_hour
print(f'Time needed: {counter_hours}h.')
