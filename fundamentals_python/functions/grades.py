grades = float(input())


def grade_fail():
    if grades < 3:
        return 'Fail'
    elif grades < 3.5:
        return 'Poor'
    elif grades < 4.5:
        return 'Good'
    elif grades < 5.5:
        return 'Very Good'
    else:
        return 'Excellent'


print(grade_fail())
