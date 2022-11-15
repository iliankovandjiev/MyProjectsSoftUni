def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_characters(name):
    for character in name:
        if not (character.isalnum() or character == '_' or character == '-'):
            return False
    return True


def no_redundant_symbols(name):
    if ' ' not in name:
        return True
    return False


def usernames_valid(name):
    if valid_length(name) and valid_characters(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(', ')
for users in usernames:
    if usernames_valid(users):
        print(users)
