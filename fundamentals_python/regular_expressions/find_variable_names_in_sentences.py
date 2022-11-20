import re

string_input = input()
pattern = r'\b_([A-Za-z0-9]+\b)'
result = re.findall(pattern, string_input)
print(','.join(result))