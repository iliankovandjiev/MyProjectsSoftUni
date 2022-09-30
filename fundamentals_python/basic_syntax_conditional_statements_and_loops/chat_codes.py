n_num = int(input())
for i in range(n_num):
    num_inp = int(input())
    if num_inp == 88:
        print('Hello')
    elif num_inp == 86:
        print('How are you?')
    elif num_inp < 88:
        print('GREAT!')
    else:
        print('Bye.')