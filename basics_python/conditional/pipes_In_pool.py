volume_pool = int(input())
debit_pipe_one = int(input())
debit_pipe_two = int(input())
hours_work = float(input())
water_in_pool = (debit_pipe_one + debit_pipe_two) * hours_work
water_from_pipe_one = debit_pipe_one * hours_work
water_from_pipe_two = debit_pipe_two * hours_work

if volume_pool >= water_in_pool:
    capacity_of_pool = water_in_pool / volume_pool
    percent_pipe_one = water_from_pipe_one / water_in_pool
    percent_pipe_two = water_from_pipe_two / water_in_pool
    print(f'The pool is {capacity_of_pool:.2%} full. Pipe 1: {percent_pipe_one:.2%}. Pipe 2: {percent_pipe_two:.2%}.')
else:
    print(f'For {hours_work} hours the pool overflows with {(water_in_pool - volume_pool):.2f} liters.')
