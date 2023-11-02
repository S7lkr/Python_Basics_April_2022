floors_n = int(input())
rooms_n = int(input())

room = 0
floor = 0
type = ''

for fl in range(floors_n, 0, -1):
    for rm in range(rooms_n):
        if fl % 2 == 0:
            type = 'O'
        else:
            type = 'A'
        if fl == floors_n:
            type = 'L'
        room = rm
        floor = fl
        print(f'{type}{floor}{room}', end=' ')
    print()