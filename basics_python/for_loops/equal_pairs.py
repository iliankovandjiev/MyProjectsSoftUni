import sys
maxdiff = 0
numbers = int(input())
sum_num = 0
max_sum = -sys.maxsize
min_sum = sys.maxsize
diff = 0
for i in range(1, numbers+1):

    num1 = int(input())
    num2 = int(input())
    sum_num = num1 + num2
    if sum_num > max_sum:
        max_sum = sum_num
    if sum_num < min_sum:
        min_sum = sum_num
    maxdiff = abs(max_sum - min_sum)
    if maxdiff != sum_num:
        diff = abs(max_sum - min_sum)
        maxdiff = sum_num

        if diff > maxdiff:
            maxdiff = diff

if maxdiff == 0:
    print(f'Yes, value={sum_num}')
else:
    print(f'No, maxdiff={maxdiff}')
