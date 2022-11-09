names_of_students = input().split(':')
courses = {}
while True:
    if len(names_of_students) < 2:
        break
    if names_of_students[2] not in courses:
        courses[names_of_students[2]] = []
    courses[names_of_students[2]].append(f'{names_of_students[0]} - {names_of_students[1]}')
    names_of_students = input().split(':')
searched_course = names_of_students[0].replace('_', ' ')
for student in courses[searched_course]:
    print(student)