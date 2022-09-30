control_number = int(input())
counter_pass = 0
password_is = 'No!'
password_is_found = False
for value_a in range(1, 10):
    for value_b in range(1, 10):
        for value_c in range(1, 10):
            for value_d in range (1, 10):
                if value_a < value_b and value_c > value_d:
                    if value_a * value_b + value_c * value_d == control_number:
                        counter_pass += 1
                        print(f'{value_a}{value_b}{value_c}{value_d}', end=' ')
                        if counter_pass == 4:
                            password_is_found = True
                            password_is = f'{value_a}{value_b}{value_c}{value_d}'
print()
if password_is_found:
    print("Password: " + password_is)
else:
    print(password_is)