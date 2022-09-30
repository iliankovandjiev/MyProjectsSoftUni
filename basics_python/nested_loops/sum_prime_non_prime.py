number = input()
prime_number = 0
nonprime_number = 0
while number != 'stop':
    number = int(number)
    if number < 0:
        print("Number is negative.")
        number = input()
    else:
        its_prime_number = True
        for i in range(2, number):
            if number % i == 0:
                its_prime_number = False
                nonprime_number += number
                break
        else:
            prime_number += number
        number = input()
print(f'Sum of all prime numbers is: {prime_number}')
print(f"Sum of all non prime numbers is: {nonprime_number}")

