numbers_of_computers = int(input())
real_sales = 0
total_sales = 0
total_rating = 0
averige_rating = 0
for computers in range (numbers_of_computers):
    command = input()
    rating = int(command[2])
    posible_sales = int(command[0] + command[1])
    if rating < 3:
        real_sales = 0
        total_sales += real_sales
    elif rating < 4:
        real_sales = posible_sales * 0.5
        total_sales += real_sales
    elif rating < 5:
        real_sales = posible_sales * 0.7
        total_sales += real_sales
    elif rating < 6:
        real_sales = posible_sales * 0.85
        total_sales += real_sales
    else:
        real_sales = posible_sales
        total_sales += real_sales
    total_rating += rating
averige_rating = total_rating / numbers_of_computers
print(f'{total_sales:.2f}')
print(f'{averige_rating:.2f}')

