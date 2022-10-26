some_text = input().split()
new_text = [word for word in some_text if len(word) % 2 == 0]
print('\n'.join(new_text))