first_half_pair_start = int(input())
second_half_pair_start = int(input())
first_diff = int(input())
second_diff = int(input())
first_half_pair_finish = first_half_pair_start + first_diff
second_half_pair_finish = second_half_pair_start + second_diff
for pair_one in range(first_half_pair_start, first_half_pair_finish + 1):
    for pair_two in range (second_half_pair_start, second_half_pair_finish + 1):
        prime_pair_one = True
        prime_pair_two = True
        for i in range(2, pair_one):
            if pair_one % i == 0:
                prime_pair_one = False
                break
        for y in range(2, pair_two):
            if pair_two % y == 0:
                prime_pair_two = False
                break
        if prime_pair_one and prime_pair_two:
            print(f'{pair_one}{pair_two}')