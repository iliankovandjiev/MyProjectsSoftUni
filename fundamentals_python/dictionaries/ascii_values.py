list_of_characters = input().split(', ')
result = {character: ord(character) for character in list_of_characters}
print(result)