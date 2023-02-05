import re


class NameTooShortError(Exception):
    """ Raise Error if name symbols are less than 4 """
    pass


class MustContainAtSymbolError(Exception):
    """ Raise Error if email don't contain @ """
    pass


class ToManyAtSymbolError(Exception):
    """ Raise Error if email contain more than one @ """
    pass


class InvalidDomainError(Exception):
    """ Raise Error if the domain isn't correct """
    pass


class InvalidPrefixesError(Exception):
    """ Raise Error if the prefix contain not allowed symbol """
    pass


while True:

    email = input('Please enter email or End: ')

    if email == 'End':
        break

    pattern_prefixes = r'^[a-z0-9]+[\.-_]?[a-z0-9]+[@]'

    if email.count('@') > 1:
        raise ToManyAtSymbolError("Email must contain only one @")
    elif not email.count('@'):
        raise MustContainAtSymbolError("Email must contain @")
    if len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    if not email.split('.')[-1] in ".com.bg.org.net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if not list(re.finditer(pattern_prefixes, email)):

        raise InvalidPrefixesError('Email format must contain only allowed symbols')

    print("Email is valid")
