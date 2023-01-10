string_input = list(input())
reverse_string = []
for _ in range(len(string_input)):
    reverse_string.append(string_input.pop())

print("".join(reverse_string))