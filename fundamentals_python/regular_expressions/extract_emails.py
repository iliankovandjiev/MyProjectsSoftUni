import re

string_input = input()
pattern = r'\s[a-z0-9]+([\.\,\-\_a-z0-9]*)@([a-z\-]+(\.[a-z\-]+)+)\b'
valid_email = re.finditer(pattern, string_input)
for email in valid_email:
    print(email.group())

