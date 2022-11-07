country_names = input().split(', ')
capital_cities = input().split(', ')
# dictionary = {country_names[index]: capital_cities[index] for index in range(len(capital_cities))}
# for country, capital in dictionary.items():
#     print(f'{country} -> {capital}')

for country, capital in zip(country_names, capital_cities):
    print(f'{country} -> {capital}')
