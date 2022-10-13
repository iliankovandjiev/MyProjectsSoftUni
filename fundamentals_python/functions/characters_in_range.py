def collect_charecter(first, second):
    single_string = []
    for char in range(ord(first_char) + 1, ord(second_char)):
        single_string.append(chr(char))
    return single_string


first_char = input()
second_char = input()
result= collect_charecter(first_char,second_char)
print(' '.join(result))