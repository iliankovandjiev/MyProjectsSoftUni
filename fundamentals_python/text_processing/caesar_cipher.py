text_to_encrypt = input()
encrypted_version = []
for char in text_to_encrypt:
    new_char = chr(ord(char) + 3)
    encrypted_version.append(new_char)
print(''.join(encrypted_version))