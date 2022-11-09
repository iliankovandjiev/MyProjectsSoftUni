numbers_of_repeat = int(input())
students = {}
for pair_of_rows in range(numbers_of_repeat):
    student_name = input()
    grade = float(input())
    if student_name not in students.keys():
        students[student_name] = []
    students[student_name].append(grade)
for student in students.keys():
    average_grade = sum(students[student]) / len(students[student])
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
