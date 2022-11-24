encrypted_message = input()
command = input().split('|')
while 'Decode' not in command:
    if command[0] == 'Move':
        index_m = command[1]
        encrypted_message = encrypted_message[int(index_m):] + encrypted_message[:int(index_m)]
    elif command[0] == 'Insert':
        index_i = command[1]
        string = command[2]
        encrypted_message = encrypted_message[:int(index_i)] + string + encrypted_message[int(index_i):]
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input().split('|')
print(f"The decrypted message is: {encrypted_message}")
