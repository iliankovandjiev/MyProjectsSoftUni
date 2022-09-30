import sys

num = int(input())
evensum = 0
oddsum = 0
oddmin = sys.maxsize
oddmax = -sys.maxsize
evenmin = sys.maxsize
evenmax = -sys.maxsize
for i in range(1, num+1):
    inp_num = float(input())
    if i % 2 == 0:
        evensum += inp_num
        if inp_num > evenmax:
            evenmax = inp_num
        if inp_num < evenmin:
            evenmin = inp_num
    else:
        oddsum += inp_num
        if inp_num > oddmax:
            oddmax = inp_num
        if inp_num < oddmin:
            oddmin = inp_num
oddsum = str(f'{oddsum:.2f}')
oddmin = str(f'{oddmin:.2f}')
oddmax = str(f'{oddmax:.2f}')
evensum = str(f'{evensum:.2f}')
evenmin = str(f'{evenmin:.2f}')
evenmax = str(f'{evenmax:.2f}')

if oddmin == str(f'{sys.maxsize:.2f}'):
    oddmin = "No"
if oddmax == str(f'{-sys.maxsize:.2f}'):
    oddmax = 'No'
if evenmax == str(f'{-sys.maxsize:.2f}'):
    evenmax = 'No'
if evenmin == str(f'{sys.maxsize:.2f}'):
    evenmin = 'No'

print(f'OddSum={oddsum},')
print(f'OddMin={oddmin},')
print(f'OddMax={oddmax},')
print(f'EvenSum={evensum},')
print(f'EvenMin={evenmin},')
print(f'EvenMax={evenmax}')