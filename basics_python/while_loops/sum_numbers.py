num_main = int(input())
num_input = int(input())
total_sum = num_input
while total_sum < num_main:
    num_input = int(input())
    total_sum += num_input
print(f'{total_sum}')