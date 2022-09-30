key = int(input())
numbers_of_lines = int(input())
for i in range(numbers_of_lines):
    letter = input()
    decrypted_letter = chr(ord(letter) + key)
    print(decrypted_letter, end='')

