name = input()
grade = 0
average = 0
count = 0
while True:
    evaluetion = float(input())
    grade += 1
    if evaluetion < 4:
        count += 1
        if count == 2:
            print(f'{name} has been excluded at {grade} grade')
            break
        grade -= 1
    else:
        average += evaluetion
    if grade == 12:
        average_grade = average / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
#
# name = input()
# grade = 1
# average = 0
# count = 0
# while grade <= 12:
#     evaluetion = float(input())
#     if evaluetion < 4:
#         count += 1
#         if count == 2:
#             print(f'{name} has been excluded at {grade} grade')
#             exit()
#     else:
#         grade += 1
#         average += evaluetion
# average_grade = average / 12
# print(f'{name} graduated. Average grade: {average_grade:.2f}')





