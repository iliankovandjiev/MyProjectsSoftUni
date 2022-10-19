import math

number_of_student = int(input())
number_of_lecture = int(input())
additional_bonus = int(input())
total_bonus_list = [0] * number_of_student
list_of_attendance = [0] * number_of_student

for attendance in range(number_of_student):
    attendance_of_student = float(input())
    total_bonus_list[attendance] += (attendance_of_student / number_of_lecture * (5 + additional_bonus))
    list_of_attendance[attendance] += attendance_of_student

if number_of_student != 0:
    max_bonus = max(total_bonus_list)
    index_of_student = total_bonus_list.index(max_bonus)
    student_attendance = list_of_attendance[index_of_student]

    print(f"Max Bonus: {math.ceil(max_bonus)}.")
    print(f"The student has attended {math.ceil(student_attendance)} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")