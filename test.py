string = input()
list_index = []

for i in range(len(string)):
    if string[i].isupper():
        list_index.extend(i)

print(list_index)