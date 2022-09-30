import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
while True:
    player_move = input('Choose [r]ock, [p]aper, [s]cissors: ')
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again...')
    computer_random_number = random.randint(1, 3)

    computer_move = ''
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f'The computer chose {computer_move}')
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('You win!')
    elif (computer_move == rock and player_move == scissors) or \
            (computer_move == paper and player_move == rock) or \
            (computer_move == scissors and player_move == paper):
        print('You lose!')
    else:
        print('Draw!')
    while True:
        answer = input('Do you want to play again y/n? ')
        if answer in ('y', 'n'):
            break
        else:
            print('Invalid input')
    if answer == 'y':
        continue
    else:
        print('Goodbay!')
        break
