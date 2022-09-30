number_of_triples = int(input())
for first_letter in range(number_of_triples):
    for second_letter in range(number_of_triples):
        for third_letter in range(number_of_triples):
            print(f'{(chr(97 + first_letter))}{(chr(97 + second_letter))}{(chr(97 + third_letter))}')