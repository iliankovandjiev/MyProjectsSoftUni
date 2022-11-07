legendary_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
item_obtained = False
while not item_obtained:
    input_items = input().split(' ')
    for index in range(0, len(input_items), 2):
        quantity = int(input_items[index])
        material = input_items[index + 1].lower()
        if material not in legendary_dict:
            legendary_dict[material] = 0
        legendary_dict[material] += quantity
        if legendary_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_dict["shards"] -= 250
            item_obtained = True
            break
        elif legendary_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_dict["fragments"] -= 250
            item_obtained = True
            break
        elif legendary_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_dict["motes"] -= 250
            item_obtained = True
            break
for material, quantity in legendary_dict.items():
    print(f"{material}: {quantity}")
