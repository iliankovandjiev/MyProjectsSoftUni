list_of_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    final_deck = []
    half_deck = (len(list_of_cards)) // 2
    left_part = list_of_cards[0:half_deck]
    right_part = list_of_cards[half_deck::]
    for index in range(len(left_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])
    list_of_cards = final_deck
print(final_deck)
