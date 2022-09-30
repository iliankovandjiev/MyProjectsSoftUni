price_mackerel = float(input())
price_sprinkle = float(input())
kilo_bonito = float(input())
kilo_safrid = float(input())
kilo_mussels = int(input())
price_bonito = 1.6 * price_mackerel
price_safrid = 1.8 * price_sprinkle
price_mussels = 7.5
total_price = kilo_bonito * price_bonito + kilo_safrid * price_safrid + kilo_mussels * price_mussels
print(f'{total_price:.2f}')

