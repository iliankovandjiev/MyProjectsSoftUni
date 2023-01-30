sequence_of_numbers = [int(num) for num in input().split()]
target_number = int(input())
for first_num in range(len(sequence_of_numbers)):
     for second_num in range(first_num + 1 , len(sequence_of_numbers)):
        if sequence_of_numbers[first_num] + sequence_of_numbers[second_num] == target_number:
            print(f'"{sequence_of_numbers[first_num]} + {sequence_of_numbers[second_num]} = {target_number}"')