movie_name = input()
ticket_student = 0
ticket_standart = 0
ticket_kids = 0
while movie_name != 'Finish':
    free_seats = int(input())
    counter_seats = 0
    for i in range(free_seats):
        type_seats = input()
        if type_seats == 'End':
            break
        elif type_seats == 'standard':
            ticket_standart += 1
        elif type_seats == 'student':
            ticket_student += 1
        elif type_seats == 'kid':
            ticket_kids += 1
        counter_seats += 1

    per_full = counter_seats / free_seats * 100
    print(f'{movie_name} - {per_full:.2f}% full.')
    movie_name = input()
total_tickets = ticket_standart + ticket_student + ticket_kids
per_ticket_standart = ticket_standart / total_tickets * 100
per_ticket_student = ticket_student / total_tickets * 100
per_ticket_kids = ticket_kids / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{per_ticket_student:.2f}% student tickets.')
print(f'{per_ticket_standart:.2f}% standard tickets.')
print(f'{per_ticket_kids:.2f}% kids tickets.')



