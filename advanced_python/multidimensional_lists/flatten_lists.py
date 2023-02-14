string_input = input().split("|")
new_string = []

for string in string_input[::-1]:
    new_string.extend(string.split())

print(*new_string)
