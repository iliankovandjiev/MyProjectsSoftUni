def even_check(number):
    if int(number) % 2 == 0:
        return True
    return False


sequence_of_numbers = input().split(' ')
even_numbers = filter(even_check, sequence_of_numbers)
even_numbers = [int(i) for i in even_numbers]
print(even_numbers)
