actor_name = str(input())
point_of_academy = float(input())
number_jury = int(input())


for i in range(1, number_jury + 1):
    name_jury = str(input())
    points = float(input())
    char = 0
    for _ in name_jury:
        char += 1
    point_of_academy += char * points / 2
    if point_of_academy >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {point_of_academy:.1f}!')
        break
else:
    needed_point = 1250.5 - point_of_academy
    print(f'Sorry, {actor_name} you need {needed_point:.1f} more!')




