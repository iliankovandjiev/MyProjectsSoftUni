from collections import deque

current_caffeine = 0

milligrams_of_coffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

while milligrams_of_coffeine and energy_drinks:
    current_milligrams = milligrams_of_coffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    caffeine = current_milligrams * current_energy_drink

    if caffeine + current_caffeine <= 300:
        current_caffeine += caffeine

    else:
        energy_drinks.append(current_energy_drink)
        if current_caffeine >= 30:
            current_caffeine -= 30
        else:
            current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")