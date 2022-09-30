input_letters = input()
secret_letters_c = False
secret_letters_o = False
secret_letters_n = False
word = ''
while input_letters != 'End':
    if 65 <= ord(input_letters) <= 90 or 97 <= ord(input_letters) <= 122:
        if input_letters == 'c':
            if secret_letters_c:
                word += input_letters
            else:
                secret_letters_c = True
        elif input_letters == 'o':
            if secret_letters_o:
                word += input_letters
            else:
                secret_letters_o = True
        elif input_letters == 'n':
            if secret_letters_n:
                word += input_letters
            else:
                secret_letters_n = True
        else:
            word += input_letters
        if secret_letters_o and secret_letters_c and secret_letters_n:
            print(word, end=" ")
            secret_letters_c = False
            secret_letters_o = False
            secret_letters_n = False
            word = ''
            input_letters = input()
        else:
            input_letters = input()
    else:
        input_letters = input()