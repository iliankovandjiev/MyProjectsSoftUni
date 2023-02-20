numbers_input = [int(x) for x in input().split()]

positive = 0
negative = 0

for num in numbers_input:
    if num < 0:
        negative += num

    elif num > 0:
        positive += num

print(negative)
print(positive)

if abs(positive) > abs(negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")