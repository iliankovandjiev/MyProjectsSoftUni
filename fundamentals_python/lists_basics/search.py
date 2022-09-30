lines_input = int(input())
word_input = input()
first_list = []
filtred_list = []
for i in range(lines_input):
    new_string = input()
    first_list.append(new_string)
print(first_list)
for string in first_list:
    if word_input in string:
        filtred_list.append(string)
print(filtred_list)
