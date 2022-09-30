first_letter = input()
second_letter = input()
no_letter = input()
first_interval = ord(first_letter)
second_interval = ord(second_letter)
no_letter_includede = ord(no_letter)
counter = 0
for one in range(first_interval, second_interval + 1):
    for two in range(first_interval, second_interval + 1):
        for three in range(first_interval, second_interval + 1):
            if one != no_letter_includede and two != no_letter_includede and three != no_letter_includede:
                counter += 1
                print(f'{chr(one)}{chr(two)}{chr((three))}', end=' ')
print(counter)