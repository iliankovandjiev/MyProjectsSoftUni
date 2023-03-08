from collections import deque

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

textiles = deque([int(x) for x in input().split(" ")])
medicaments = deque([int(x) for x in input().split(" ")])
created_item = []
left_medicament = True
left_textile = True

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    healing_item = textile + medicament

    if healing_items.get(healing_item):
        created_item.append(healing_items[healing_item])
    elif healing_item > 100:
        created_item.append("MedKit")
        new_value = healing_item - 100
        if medicaments:
            medicaments.append(medicaments.pop() + new_value)
        else:
            medicaments.append(new_value)
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and medicaments:
    print("Textiles are empty.")
    left_textile = False
elif not medicaments and textiles:
    print("Medicaments are empty.")
    left_medicament = False
elif not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
    left_medicament = False
    left_textile = False

if created_item:
    text_to_print = set(created_item)
    for item in sorted(text_to_print):
        print(item)