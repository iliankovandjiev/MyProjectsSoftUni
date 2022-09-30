num_cargo = int(input())
microbus = 0
truck = 0
train = 0
price = 0
total_ton = 0
for i in range(num_cargo):
    ton_cargo = int(input())
    if ton_cargo <= 3:
        microbus += ton_cargo
        total_ton += ton_cargo
        price += ton_cargo * 200
    elif ton_cargo <= 11:
        truck += ton_cargo
        total_ton += ton_cargo
        price += ton_cargo * 175
    else:
        train += ton_cargo
        total_ton += ton_cargo
        price += ton_cargo * 120
med_price = price / total_ton
per_microbus = microbus / total_ton * 100
per_truck = truck / total_ton * 100
per_train = train / total_ton * 100
print(f'{med_price:.2f}')
print(f'{per_microbus:.2f}%')
print(f'{per_truck:.2f}%')
print(f'{per_train:.2f}%')