import re

name_input = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
filtered_names = re.findall(pattern, name_input)
print(' '.join(filtered_names))
