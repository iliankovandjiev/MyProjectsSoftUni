x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
if x1 >= x2 or y1 >= y2:
    print('Error')
else:
    if (x == x1 and y1 <= y <= y2):
        print('Border')
    elif (x == x2 and y1 <= y <= y2):
        print('Border')
    elif (y == y1 and x1 <= x <= x2):
        print('Border')
    elif (y == y2 and x1 <= x <= x2):
        print('Border')
    else:
        print('Inside / Outside')