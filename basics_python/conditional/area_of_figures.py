from math import pi
type_of_figure = str(input())
# dimension_one = float(input())
# dimension_two = float(input())
if type_of_figure == "square":
    dimension_one = float(input())
    area_square = dimension_one ** 2
    print(f'{area_square:.3f}')
elif type_of_figure == "rectangle":
    dimension_one = float(input())
    dimension_two = float(input())
    area_rectangle = dimension_two * dimension_one
    print(f'{area_rectangle:.3f}')
elif type_of_figure == "circle":
    dimension_one = float(input())
    area_circle = pi * dimension_one ** 2
    print(f'{area_circle:.3f}')
elif type_of_figure == "triangle":
    dimension_one = float(input())
    dimension_two = float(input())
    area_triangle = dimension_one * dimension_two / 2
    print(f'{area_triangle:.3f}')


