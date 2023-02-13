symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("files_exercise/text.txt", "r") as even_lines_text:
    text = even_lines_text.readlines()

for line in range(0, len(text), 2):

    for symbol in symbols_to_replace:
        text[line] = text[line].replace(symbol, "@")

    new_text = text[line][:-1].split(" ")
    print(" ".join(str(text) for text in reversed(new_text)))