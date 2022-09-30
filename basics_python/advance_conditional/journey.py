budget = float(input())
season = str(input())
spend_budget = 0
destination = ''
sleep = ''
if budget <= 100:
    if season == 'summer':
        destination = 'Bulgaria'
        sleep = 'Camp'
        spend_budget = budget * 0.3
    elif season == 'winter':
        destination = 'Bulgaria'
        sleep = 'Hotel'
        spend_budget = budget * 0.7
elif budget <= 1000:
    if season == 'summer':
        destination = 'Balkans'
        sleep = 'Camp'
        spend_budget = budget * 0.4
    elif season == 'winter':
        destination = 'Balkans'
        sleep = 'Hotel'
        spend_budget = budget * 0.8
else:
    destination = 'Europe'
    sleep = 'Hotel'
    spend_budget = budget * 0.9
print(f"Somewhere in {destination}")
print(f'{sleep} - {spend_budget:.2f}')