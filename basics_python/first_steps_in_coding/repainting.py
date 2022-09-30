nailon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())
total_sum = ((nailon + 2) * 1.5) + paint * 1.1 * 14.5 + diluent * 5 + 0.4
work = total_sum * 0.3 * hours
print(total_sum + work)

