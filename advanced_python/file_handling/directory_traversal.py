import os


def save_file_extension(name):
    for filename in os.listdir(name):

        if os.path.isfile(filename):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)


file_directory = input()
extensions = {}
save_file_extension(file_directory)

for exten in sorted(extensions.keys()):
    with open("report.txt", "a") as file:
        file.write(f".{exten}\n")
    for filenames in sorted(extensions[exten]):
        with open("report.txt", "a") as file:
            file.write(f"- - - {filenames}\n")

