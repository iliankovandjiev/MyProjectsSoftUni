import math

square_vineyard = int(input())
grape = float(input())
needed_litres = int(input())
number_workers = int(input())
vine = square_vineyard * 0.4
kilos_grape = vine * grape
litre_vine = kilos_grape / 2.5
vine_total = abs(litre_vine - needed_litres)
if litre_vine < needed_litres:
    print(f'It will be a tough winter! More {math.floor(vine_total)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(litre_vine)} liters.')
    print(f'{math.ceil(vine_total)} liters left -> {math.ceil(vine_total / number_workers)} liters per person.')