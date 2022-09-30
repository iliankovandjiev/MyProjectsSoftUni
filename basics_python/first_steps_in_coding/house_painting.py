x_house = float(input())
y_house = float(input())
h_house = float(input())
area_roof = 2 * (x_house * y_house) + x_house * h_house
area_wall = (2 * x_house ** 2 - 1.2 * 2) + 2 * x_house * y_house - (2 * 1.5 **2)
consumption_green = area_wall / 3.4
consumption_red = area_roof / 4.3
print(f'{consumption_green:.2f}')
print(f'{consumption_red:.2f}')

