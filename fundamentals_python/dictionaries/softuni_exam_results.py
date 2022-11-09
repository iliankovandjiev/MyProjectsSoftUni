command = input()
students_result = {}
language_result = {}
while command != 'exam finished':
    splitted_command = command.split('-')
    if "banned" in splitted_command:
        username, banned = splitted_command
        students_result.pop(username)
    else:
        username, language, points = splitted_command
        if username not in students_result.keys():
            students_result[username] = int(points)
        else:
            if students_result[username] < int(points):
                students_result[username] = int(points)
        if language not in language_result.keys():
            language_result[language] = 0
        language_result[language] += 1

    command = input()
print('Results:')
for student, point in students_result.items():
    print(f'{student} | {point}')
print('Submissions:')
for language_name, numbers_of_submission in language_result.items():
    print(f'{language_name} - {numbers_of_submission}')
