n_start = int(input())
n_end = int(input())

for a in range(n_start, n_end+1):
    for b in range(n_start, n_end + 1):
        for c in range(n_start, n_end + 1):
            for d in range(n_start, n_end + 1):
                plate = f'{a}{b}{c}{d}'
                if a > d and (b+c) % 2 == 0:
                    if a % 2 == 0 and d % 2 != 0:
                        print(plate, end=' ')
                    elif a % 2 != 0 and d % 2 == 0:
                        print(plate, end=' ')