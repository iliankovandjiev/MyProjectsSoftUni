import os

while True:

    command, *info = input().split("-")
    if command == "End":
        break

    elif command == "Create":
        file = open(f"files_exercise/{info[0]}", "w")
        file.close()

    elif command == "Add":
        with open(f"files_exercise/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"files_exercise/{info[0]}", "r") as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(info[1], info[2])

            with open(f"files_exercise/{info[0]}", "w") as file:
                file.write("".join(text))

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"files_exercise/{info[0]}")
        except FileNotFoundError:
            print("An error occurred")
