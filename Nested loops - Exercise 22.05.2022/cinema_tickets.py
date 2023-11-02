movie = input()

total_ticket_cnt = 0
ticket_cnt = 0
student = 0
standard = 0
kids = 0
ready_to_start = False

while movie != 'Finish':
    seats = int(input())
    while ticket_cnt < seats:
        ticket_type = input()
        if ticket_type == 'End':
            ready_to_start = True
            break
        elif ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kids += 1
        ticket_cnt += 1
        total_ticket_cnt += 1

    if ready_to_start or ticket_cnt >= seats:
        print(f'{movie} - {(ticket_cnt / seats) * 100:.2f}% full.')
    ticket_cnt = 0
    movie = input()

print(f'Total tickets: {total_ticket_cnt}')
print(f'{(student / total_ticket_cnt) * 100:.2f}% student tickets.')
print(f'{(standard / total_ticket_cnt) * 100:.2f}% standard tickets.')
print(f'{(kids / total_ticket_cnt) * 100:.2f}% kids tickets.')