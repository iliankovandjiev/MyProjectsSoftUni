def students_credits(*args):
    courses = {}
    final_string = []
    total_point = 0

    for string in args:
        course_name, credit, max_test_point, diyan_point = string.split("-")
        achived_credit = (int(diyan_point) / int(max_test_point)) * int(credit)
        total_point += achived_credit
        courses[course_name] = float(f"{achived_credit:.1f}")

    if total_point >= 240:
        final_string.append(f"Diyan gets a diploma with {total_point:.1f} credits.")
        for course, point in sorted(courses.items(), key=lambda x: -x[1]):
            final_string.append(f"{course} - {point}")
    else:
        final_string.append(f"Diyan needs {240 - total_point:.1f} credits more for a diploma.")
        for course, point in sorted(courses.items(), key=lambda x: -x[1]):
            final_string.append(f"{course} - {point}")

    return "\n".join(final_string)

