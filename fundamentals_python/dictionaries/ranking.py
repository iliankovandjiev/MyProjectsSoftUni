from operator import itemgetter
command1 = input()
contest_dict = {}
candidate_dict = {}
while command1 != 'end of contests':
    contest, password_for_contest = command1.split(':')
    contest_dict[contest] = password_for_contest
    command1 = input()
command2 = input()
while command2 != 'end of submissions':
    contest, password, username, points = command2.split('=>')
    if contest in contest_dict.keys():
        if password in contest_dict.values():
            if username not in candidate_dict:
                candidate_dict[username] = {contest: int(points)}
            else:
                if contest in candidate_dict[username].keys():
                    if int(points) > candidate_dict[username][contest]:
                        candidate_dict[username] = {contest: int(points)}
                else:
                    candidate_dict[username][contest] = int(points)
    command2 = input()
total_score = 0
candidate_name = ''
for candidate in candidate_dict.keys():
    candidate_score = 0
    for language, score in candidate_dict[candidate].items():
        candidate_score += score
    if candidate_score > total_score:
        total_score = candidate_score
        candidate_name = candidate
print(f'Best candidate is {candidate_name} with total {total_score} points.')
print('Ranking:')
for candidate in sorted(candidate_dict.keys()):
    print(candidate)
    sorted_candidate_dict = sorted(candidate_dict[candidate].items(), key=itemgetter(1))
    for contest, points in reversed(sorted_candidate_dict):
        print(f'#  {contest} -> {points}')
