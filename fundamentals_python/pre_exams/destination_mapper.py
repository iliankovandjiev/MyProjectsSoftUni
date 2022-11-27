import re

destinations = input()
list_of_destinations = []
travel_point = 0
pattern = r'(\=|\/)([A-Z][A-Za-z][A-Za-z]+)\1'
final_destinations = re.findall(pattern, destinations)
for destination in final_destinations:
    list_of_destinations.append(destination[1])
    travel_point += len(destination[1])
print(f"Destinations: {', '.join(list_of_destinations)}")
print(f"Travel Points: {travel_point}")