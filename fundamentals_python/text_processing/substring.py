string_for_remove = input()
string_to_remove = input()
while string_for_remove in string_to_remove:
    string_to_remove = string_to_remove.replace(string_for_remove, '')
print(string_to_remove)
