year_input = int(input())
happy_year = False
while not happy_year:
    year_input += 1
    year_set = set(str(year_input))
    if len(str(year_input)) == len(year_set):
        happy_year = True


print(year_input)