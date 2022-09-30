
num_tab = int(input())
salary = float(input())
for i in range(1, num_tab+1):
    internet = str(input())
    if internet == 'Facebook':
        salary -= 150
    elif internet == 'Instagram':
        salary -= 100
    elif internet == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(f'{salary:.0f}')




