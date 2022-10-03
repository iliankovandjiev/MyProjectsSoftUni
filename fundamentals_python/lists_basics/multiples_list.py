factor = int(input())
count_number = int(input())
list_number= []
for value in range(1, count_number + 1):
    list_number.append(value * factor)
print(list_number)