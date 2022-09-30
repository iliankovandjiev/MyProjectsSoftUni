# # for right triangle
# input_number = int(input())
# for row in range(input_number):
#     for columns in range(row + 1):
#         print('*', end='')
#     print()
#

#for left triangle
# input_number = int(input())
# for row in range(input_number):
#     for columns in range(row, input_number - 1):
#         print('*', end=' ')
#     print()


#for hill pattern
# input_number = int(input())
# for row in range(input_number):
#     for columns in range(row, input_number - 1):
#         print('', end=' ')
#     for columns in range(row):
#         print('*', end='')
#     for columns in range(row):
#         print('*', end='')
#     print()

#for revers pattern
input_number = int(input())
for row in range(input_number):
    for columns in range(row):
        print(' ', end='')
    for columns in range(row, input_number - 1):
        print('*', end='')
    for columns in range(row, input_number):
        print('*', end='')
    print()



# for dimond pattern
# input_number = int(input())
# for row in range(input_number - 1):
#     for columns in range(row, input_number - 1):
#         print('', end=' ')
#     for columns in range(row):
#         print('*', end='')
#     for columns in range(row + 1):
#         print('*', end='')
#     print()
# for row in range(input_number):
#     for columns in range(row):
#         print(' ', end='')
#     for columns in range(row, input_number - 1):
#         print('*', end='')
#     for columns in range(row, input_number):
#         print('*', end='')
#     print()
