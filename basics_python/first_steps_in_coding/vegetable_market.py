price_vege = float(input())
price_fruit = float(input())
total_kilo_vege = int(input())
total_kilo_fruit = int(input())
total_leva = price_fruit * total_kilo_fruit + price_vege * total_kilo_vege
total_euro = total_leva / 1.94
print(f'{total_euro:.2f}')
