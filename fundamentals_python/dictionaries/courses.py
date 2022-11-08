command = input()
course_register = {}
while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in course_register.keys():
        course_register[course_name] = []
    course_register[course_name].append(student_name)
    command = input()
for courses in course_register.keys():
    print(f"{courses}: {len(course_register[courses])}")
    for student in course_register[courses]:
        print(f"-- {student}")
