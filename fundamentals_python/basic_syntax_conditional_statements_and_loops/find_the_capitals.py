single_string = input()
list_index = []
for lower in range(len(single_string)):
    if single_string[lower].isupper():
        list_index.append(lower)
print(list_index)






