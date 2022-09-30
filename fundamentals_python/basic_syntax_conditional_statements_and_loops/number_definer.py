num_input = float(input())
if num_input == 0:
    print('zero')
elif num_input < 0:
    if abs(num_input) < 1:
        print('small negative')
    elif abs(num_input) > 1000000:
        print('large negative')
    else:
        print('negative')
else:
    if num_input < 1:
        print('small positive')
    elif num_input > 1000000:
        print('large positive')
    else:
        print('positive')

