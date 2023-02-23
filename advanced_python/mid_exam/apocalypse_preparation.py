from collections import deque

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

textiles = deque([int(x) for x in input().split(" ")])
medicaments = deque([int(x) for x in input().split(" ")])
created_item = {}
left_medicament = True
left_textile = True

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    healing_item = textile + medicament

    if healing_item in healing_items.keys():
        if healing_items[healing_item] not in created_item:
            created_item[healing_items[healing_item]] = 0
        created_item[healing_items[healing_item]] += 1
    elif healing_item > 100:
        if "MedKit" not in created_item.keys():
            created_item["MedKit"] = 0
        created_item["MedKit"] += 1
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
else:
    print("Textiles and medicaments are both empty.")
    left_medicament = False
    left_textile = False

if created_item:
    for item, ele in sorted(created_item.items(), key=lambda x: (-x[1], x[0])):
        print(f'{item} - {ele}')

if left_textile:

    text_to_print = [str(x) for x in textiles]

    print(f"Textiles left: {', '.join(text_to_print)}")
elif left_medicament:
    text_to_print = [str(x) for x in medicaments]

    print(f"Medicaments left: {', '.join(text_to_print[::-1])}")