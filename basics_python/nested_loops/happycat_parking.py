day_number = int(input())
clock_count = int(input())
total = 0
tax_parking = 0
hours_count = 0
for day in range(1 , day_number + 1):
    day_tax = 0
    for hours in range (1, clock_count + 1):
        if day % 2 == 0 and hours % 2 != 0:
            tax_parking = 2.5
            day_tax += tax_parking
        elif day % 2 != 0 and hours % 2 == 0:
            tax_parking = 1.25
            day_tax += tax_parking
        else:
            tax_parking = 1
            day_tax += tax_parking
    total += day_tax
    print(f"Day: {day} - {day_tax:.2f} leva")
print(f"Total: {total:.2f} leva")
