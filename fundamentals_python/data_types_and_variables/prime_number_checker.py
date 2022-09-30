number_input = int(input())
prime = True
for divisor in range (2, number_input):
    if number_input % divisor == 0:
        prime = False
if prime:
    print('True')
else:
    print('False')