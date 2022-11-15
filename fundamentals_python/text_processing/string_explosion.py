data = input()
string_after_explosion = ''
strength = 0
for index in range(len(data)):
    if strength > 0 and data[index] != '>':
        strength -= 1
    elif data[index] == '>':
        string_after_explosion += data[index]
        strength += int(data[index + 1])
    else:
        string_after_explosion += data[index]
print(string_after_explosion)
