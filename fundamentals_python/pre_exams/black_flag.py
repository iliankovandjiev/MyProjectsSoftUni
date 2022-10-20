days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder_gather = 0

for days in range(1, days_of_plunder + 1):
    plunder_gather += daily_plunder

    if days % 3 == 0:
        plunder_gather += 0.5 * daily_plunder

    if days % 5 == 0:
        plunder_gather -= 0.3 * plunder_gather

if plunder_gather >= expected_plunder:
    print(f"Ahoy! {plunder_gather:.2f} plunder gained.")
else:
    percentage_left = (plunder_gather / expected_plunder) * 100
    print(f"Collected only {percentage_left:.2f}% of the plunder.")