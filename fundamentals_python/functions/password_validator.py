def is_valid(password):
    pass_is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False
    counter = 0
    for letter in password:
        if letter.isdigit():
            counter += 1
    if not counter >= 2:
        print('Password must have at least 2 digits')
        pass_is_valid = False
    return pass_is_valid


input_password = input()
pass_is_valid = is_valid(input_password)
if pass_is_valid:
    print("Password is valid")
