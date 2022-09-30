n_inputs = int(input())
total_sum = 0
for i in range(n_inputs):
    letter_input = input()
    total_sum += ord(letter_input)
print(f'The sum equals: {total_sum}')
