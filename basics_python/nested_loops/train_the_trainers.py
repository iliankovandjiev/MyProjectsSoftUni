jury = int(input())
presentation = input()
total_presentation = 0
total_grade = 0
while presentation != 'Finish':
    total_presentation += 1
    current_presentation = 0
    for i in range(jury):
        grade = float(input())
        current_presentation += grade
    average_grade = current_presentation / jury
    total_grade += average_grade
    print(f'{presentation} - {average_grade:.2f}.')
    presentation = input()
average_total_grade = total_grade / total_presentation
print(f"Student's final assessment is {average_total_grade:.2f}.")