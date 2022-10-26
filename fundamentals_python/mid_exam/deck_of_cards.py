deck_of_cards = input().split(', ')
number_input = int(input())
for cards in range(number_input):
    command = input()

    if 'Add' in command:
        add_command, card_name = command.split(', ')
        if card_name not in deck_of_cards:
            deck_of_cards.append(card_name)
            print('Card successfully added')
        else:
            print('Card is already in the deck')

    elif 'Remove At' in command:
        remove_at_command, index = command.split(', ')
        if 0 < int(index) <= len(deck_of_cards):
            deck_of_cards.pop(int(index))
            print('Card successfully removed')
        else:
            print('Index out of range')

    elif 'Remove' in command:
        remove_command, card_name = command.split(', ')
        if card_name in deck_of_cards:
            deck_of_cards.remove(card_name)
            print('Card successfully removed')
        else:
            print('Card not found')

    elif 'Insert' in command:
        insert_command, index, card_name = command.split(', ')
        if 0 < int(index) <= len(deck_of_cards):
            if card_name in deck_of_cards:
                print('Card is already added')
            else:
                deck_of_cards.insert(int(index), card_name)
                print('Card successfully added')
        else:
            print('Index out of range')
print(', '.join(deck_of_cards))
