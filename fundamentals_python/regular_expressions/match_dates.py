import re

date_input = input()
valid_date_pattern = r'\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b'
valid_date = re.findall(valid_date_pattern, date_input)
for match in valid_date:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')