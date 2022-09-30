total_person = int(input())
capacity = int(input())
total_courses = 0
total_courses += total_person // capacity
if total_person % capacity != 0:
    total_courses += 1
print(total_courses)