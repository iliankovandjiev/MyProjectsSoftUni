count_of_the_words = int(input())
synonyms_dict = {}
for _ in range(count_of_the_words):
    word = input()
    synonym = input()
    if word not in synonyms_dict.keys():
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)
for words, synonyms in synonyms_dict.items():
    print(f'{words} - {", ".join(synonyms_dict[words])}')

