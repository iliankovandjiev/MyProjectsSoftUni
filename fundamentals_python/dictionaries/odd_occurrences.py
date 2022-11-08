sequence_of_words = input().split()
dictionary = {}
for word in sequence_of_words:
    word = word.lower()
    if word not in dictionary.keys():
        dictionary[word] = 0
    dictionary[word] += 1
for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')

