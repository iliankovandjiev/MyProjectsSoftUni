book = input()
input_book = input()
count = 0
while book != input_book:
    if input_book == "No More Books":
        break
    count += 1
    input_book = input()
if input_book == "No More Books":
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')
else:
    print(f'You checked {count} books and found it.')
