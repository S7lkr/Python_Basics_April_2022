men = int(input())
women = int(input())
tables = int(input())
no_more_people = False

tables_cnt = 0

for m in range(1, men+1):
    for w in range(1, women+1):
        if tables_cnt < tables:
            meeting = f'({m} <-> {w})'
            print(meeting, end=' ')
            tables_cnt += 1
        else:
            break