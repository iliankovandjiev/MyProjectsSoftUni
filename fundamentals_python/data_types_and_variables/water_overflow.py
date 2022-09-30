numbers_of_inputs= int(input())
total_capacity = 255
for i in range(numbers_of_inputs):
    litter_input = int(input())
    total_capacity -= litter_input
    if total_capacity < 0:
        print('Insufficient capacity!')
        total_capacity += litter_input
print(255 - total_capacity)
