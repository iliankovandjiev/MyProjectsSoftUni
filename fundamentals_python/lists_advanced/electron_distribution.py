number_of_electrons = int(input())
shell = 0
list_of_shells = []
while number_of_electrons > 0:
    shell += 1
    filling_shell = 2 * (shell ** 2)
    if filling_shell <= number_of_electrons:
        number_of_electrons -= filling_shell
        list_of_shells.append(filling_shell)
    else:
        list_of_shells.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
print(list_of_shells)


