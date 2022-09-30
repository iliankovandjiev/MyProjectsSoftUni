mens = int(input())
woman = int(input())
total_tables = int(input())
man_counter = 0
woman_counter = 0
table_counter = 0
for mans_dating in range(1, mens + 1):
    for woman_dating in range(1, woman + 1):
        table_counter += 1
        if table_counter <= total_tables:
            print(f'({mans_dating} <-> {woman_dating})', end=' ')
        else:
            break