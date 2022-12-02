password = input()
new_password = ''
while True:
    command = input()
    if command == 'Done':
        break
    command = command.split(' ')
    if command[0] == 'TakeOdd':
        for index, symbol in enumerate(password):
            if index % 2 != 0:
                new_password += symbol
        password = new_password
        print(password)
    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[(index + length):]
        print(password)
    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")
