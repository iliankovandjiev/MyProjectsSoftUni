import string

file = open("files_exercise/text.txt", "r")


text = file.readlines()
count_of_line = 0

for line in text:
    punctuation_marks = 0
    total_letters = 0
    count_of_line += 1

    for letter in line:
        if letter.isalpha():
            total_letters += 1
        elif letter in string.punctuation:
            punctuation_marks += 1

    new_file = open("files_exercise/output.txt", "a")
    new_file.write(f"Line {count_of_line}: {line[:-1]} ({total_letters})({punctuation_marks})\n")
    new_file.close()

file.close()
