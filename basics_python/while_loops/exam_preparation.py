low_grades = int(input())
name_task = input()
num_task = 0
last_problem = name_task
count_grade = 0
total_grade = 0
while name_task != 'Enough':
    grade = int(input())
    total_grade += grade
    num_task += 1
    last_problem = name_task
    if grade <= 4:
        count_grade += 1
    if count_grade == low_grades:
        break
    name_task = input()
if count_grade == low_grades:
    print(f'You need a break, {low_grades} poor grades.')
else:
    average_grade = total_grade / num_task
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {num_task}')
    print(f'Last problem: {last_problem}')