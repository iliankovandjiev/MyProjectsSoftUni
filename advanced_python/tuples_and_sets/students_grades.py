number_of_students = int(input())
student_name_and_grade = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in student_name_and_grade:
        student_name_and_grade[student] = []
    student_name_and_grade[student].append(float(grade))

for student_name, grade_all in student_name_and_grade.items():
    average_grade = sum(grade_all) / len(grade_all)
    list_of_grades = (' '.join(map(lambda grade: f'{grade:.2f}', grade_all)))
    print(f"{student_name} -> {list_of_grades} (avg: {average_grade:.2f})")

