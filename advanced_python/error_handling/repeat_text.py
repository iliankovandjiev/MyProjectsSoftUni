text_input = input()
try:
    times_for_repeat = int(input())
    print(text_input * times_for_repeat)

except ValueError as error:
    print("Variable times must be an integer")
